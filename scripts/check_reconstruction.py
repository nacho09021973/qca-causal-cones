"""Check that a typographic reconstruction only restores backslashes.

Usage (from the repo root):
    python3 -B scripts/check_reconstruction.py <path> [<base_commit>]

<base_commit> defaults to 2d144d9 (the logged mechanical repair). The check
removes the leading "> **Typographic reconstruction" blockquote from the
working-tree file, deletes every backslash from both versions, and requires
the results to be identical (a restored "\\n" before a letter counts as the
newline it became). Thus the reconstruction may add backslashes (and
nothing else) relative to the corrupted text. Exits 1 and prints the first
difference otherwise. See reports/2026-10-22--escape-corruption-audit.md.

Opt-in --allow-lost-cr-newlines additionally normalizes restored r commands
to LF plus their suffix, for the logged CR-to-LF corruption in CURRENT_STATE.
It is off by default and must be paired with explicit provenance for that file.
"""

import difflib
import argparse
import re
import subprocess
import sys


def strip_header(text):
    lines = text.split("\n")
    out, i = [], 0
    while i < len(lines):
        if lines[i].startswith("> **Typographic reconstruction"):
            while i < len(lines) and lines[i].startswith(">"):
                i += 1
            if i < len(lines) and lines[i] == "":
                i += 1
            continue
        out.append(lines[i])
        i += 1
    return "\n".join(out)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    parser.add_argument("base", nargs="?", default="2d144d9")
    parser.add_argument("--allow-lost-cr-newlines", action="store_true",
                        help="Explicitly allow restored LaTeX r commands whose CR became LF")
    args = parser.parse_args()
    path, base = args.path, args.base
    old = subprocess.run(["git", "show", f"{base}:{path}"], capture_output=True,
                         check=True).stdout.decode("utf-8")
    new = open(path, encoding="utf-8", newline="").read()
    # A restored "\\n<letter>" (e.g. \\neq, \\nabla) corresponds to a newline
    # in the corrupted text; normalize it identically on both sides.
    def norm(s):
        s = re.sub(r"\\n(?=[A-Za-z])", "\n", s)
        if args.allow_lost_cr_newlines:
            s = re.sub(r"\\r(?=[A-Za-z])", "\n", s)
        return s.replace("\\", "")
    a = norm(old)
    b = norm(strip_header(new))
    if a == b:
        qualifier = " (including logged CR-to-LF restoration)" if args.allow_lost_cr_newlines else ""
        print(f"[PASS] {path}: differs from {base} only by backslashes{qualifier}")
        return 0
    diff = difflib.unified_diff(a.split("\n"), b.split("\n"), "base", "reconstruction",
                                lineterm="", n=1)
    print(f"[FAIL] {path}: changes beyond backslashes")
    for k, line in enumerate(diff):
        if k > 40:
            break
        print(line)
    return 1


if __name__ == "__main__":
    sys.exit(main())
