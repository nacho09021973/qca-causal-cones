"""Detect and repair escape-sequence corruption in tracked text documents.

Background (2026-10-22): documents committed on 2026-09-29/30 through a JSON or
string-escape layer lost LaTeX backslashes: "\\boxed" became BS+"oxed",
"\\frac" FF+"rac", "\\text" TAB+"ext", "\\rangle" a lone CR+"angle", and "\\nabla"
a newline followed by "abla". Backslashes before other letters ("\\omega",
"\\[") were stripped without trace; only the control-character cases are
mechanically repairable, the rest needs manual reconstruction.
See reports/2026-10-22--escape-corruption-audit.md.

Usage (from the repo root):
    python3 -B scripts/text_integrity.py --check
        Exit 1 if any tracked .md/.tex file contains a control character other
        than newline (TAB is allowed only when not followed by a letter), or a
        line listed as a suspected lost "\\n" that is not resolved in the
        decisions file. Run before every commit that adds text.
    python3 -B scripts/text_integrity.py --repair --log <path.tsv>
        Restore BS/FF/BEL/VT and TAB+letter to backslash+letter, apply the
        newline decisions in scripts/text_integrity_newline_decisions.tsv, and
        write one log row per change.
    python3 -B scripts/text_integrity.py --list-newline-suspects
        Print candidate lost-"\\n" joins for manual decision.

The decisions file has rows: path<TAB>line_number_of_suspect_line<TAB>JOIN|KEEP,
where line numbers refer to the file before any newline join in this run.
JOIN restores "\\n" + suspect line onto the previous line.
"""

import argparse
import re
import subprocess
import sys

CONTROL_MAP = {"\x07": "\\a", "\x08": "\\b", "\x0b": "\\v", "\x0c": "\\f"}
SUSPECT_START = re.compile(
    r"^(abla|eq\b|eq[ _^{]|ot[ {\\=]|u[_^ ]|ewline|ewcommand|ormalsize|ewpage)")
DECISIONS = "scripts/text_integrity_newline_decisions.tsv"


def tracked_text_files():
    out = subprocess.run(["git", "ls-files", "*.md", "*.tex"], capture_output=True,
                         text=True, check=True).stdout.split("\n")
    return [p for p in out if p]


def load_decisions():
    dec = {}
    try:
        with open(DECISIONS, encoding="utf-8") as f:
            for row in f:
                if row.startswith("#") or not row.strip():
                    continue
                path, line, action = row.rstrip("\n").split("\t")[:3]
                dec[(path, int(line))] = action
    except FileNotFoundError:
        pass
    return dec


def newline_suspects(path, text):
    lines = text.split("\n")
    sus = []
    for i, line in enumerate(lines[1:], start=2):
        if SUSPECT_START.match(line):
            sus.append((i, lines[i - 2][-60:], line[:60]))
    return sus


def bad_chars(text):
    found = []
    for i, ch in enumerate(text):
        if ch in CONTROL_MAP or is_lone_cr(text, i):
            found.append((i, ch))
        elif ch == "\t" and i + 1 < len(text) and text[i + 1].isalpha():
            found.append((i, ch))
    return found


def is_lone_cr(text, i):
    # CRLF line endings are legitimate; a CR not followed by LF is a lost "\r".
    return text[i] == "\r" and (i + 1 >= len(text) or text[i + 1] != "\n")


def line_of(text, pos):
    return text.count("\n", 0, pos) + 1


def bare_display_lines(text):
    """Bare math delimiters outside Markdown fenced code (where ] is valid code).

    Control-character and lost-newline checks deliberately still inspect code.
    """
    fence_char, fence_len = None, 0
    for ln, line in enumerate(text.split("\n"), start=1):
        fence = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if fence:
            marker, tail = fence.groups()
            if fence_char is None:
                fence_char, fence_len = marker[0], len(marker)
            elif marker[0] == fence_char and len(marker) >= fence_len and not tail.strip():
                fence_char = None
            continue
        if fence_char is None and line.strip() in ("[", "]"):
            yield ln


def check():
    dec = load_decisions()
    problems = 0
    for path in tracked_text_files():
        text = open(path, encoding="utf-8", errors="replace", newline="").read()
        for pos, ch in bad_chars(text):
            print(f"{path}:{line_of(text, pos)}: control {ch!r}")
            problems += 1
        for ln, _, cur in newline_suspects(path, text):
            if dec.get((path, ln)) != "KEEP":
                print(f"{path}:{ln}: suspected lost \\n before {cur[:30]!r}")
                problems += 1
        # Display-math delimiters reduced to a bare "[" or "]" line indicate that
        # non-escape backslashes were stripped; these are not mechanically repairable.
        for ln in bare_display_lines(text):
            print(f"{path}:{ln}: bare display delimiter (stripped backslashes)")
            problems += 1
    print(f"{problems} problem(s)")
    return 1 if problems else 0


def repair(log_path):
    dec = load_decisions()
    rows = []
    for path in tracked_text_files():
        text = open(path, encoding="utf-8", newline="").read()
        orig = text
        # 1) newline joins first, using original line numbers
        lines = text.split("\n")
        joins = sorted(ln for (p, ln), a in dec.items() if p == path and a == "JOIN")
        for ln in reversed(joins):
            prev, cur = lines[ln - 2], lines[ln - 1]
            assert SUSPECT_START.match(cur), (path, ln, cur)
            lines[ln - 2:ln] = [prev + "\\n" + cur]
            rows.append((path, str(ln), "LF", "\\n", cur[:40]))
        text = "\n".join(lines)
        # 2) control characters
        out = []
        for i, ch in enumerate(text):
            if ch in CONTROL_MAP or is_lone_cr(text, i):
                rep = CONTROL_MAP.get(ch, "\\r")
                out.append(rep)
                rows.append((path, str(line_of(text, i)), repr(ch), rep,
                             text[i + 1:i + 25].replace("\t", " ").replace("\n", " ")
                             .replace("\r", " ")))
            elif ch == "\t" and i + 1 < len(text) and text[i + 1].isalpha():
                out.append("\\t")
                rows.append((path, str(line_of(text, i)), "'\\t'", "\\t",
                             text[i + 1:i + 25].replace("\t", " ").replace("\n", " ")))
            else:
                out.append(ch)
        text = "".join(out)
        if text != orig:
            with open(path, "w", encoding="utf-8", newline="") as f:
                f.write(text)
    with open(log_path, "w", encoding="utf-8") as f:
        f.write("path\tline\tfound\trestored\tfollowing_text\n")
        for r in rows:
            f.write("\t".join(r) + "\n")
    print(f"{len(rows)} change(s); log: {log_path}")
    return 0


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--check", action="store_true")
    g.add_argument("--repair", action="store_true")
    g.add_argument("--list-newline-suspects", action="store_true")
    ap.add_argument("--log")
    a = ap.parse_args()
    if a.check:
        sys.exit(check())
    if a.repair:
        if not a.log:
            ap.error("--repair needs --log")
        sys.exit(repair(a.log))
    for path in tracked_text_files():
        text = open(path, encoding="utf-8", errors="replace", newline="").read()
        for ln, prev, cur in newline_suspects(path, text):
            print(f"{path}\t{ln}\t...{prev!r}\t|\t{cur!r}")


if __name__ == "__main__":
    main()
