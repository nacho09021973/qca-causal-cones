"""Check that a typographic reconstruction only restores backslashes.

Usage (from the repo root):
    python3 -B scripts/check_reconstruction.py <path> [<base_commit>]

<base_commit> defaults to 2d144d9 (the logged mechanical repair). The check
removes the leading "> **Typographic reconstruction" blockquote from the
working-tree file, deletes every backslash from both versions, and requires
the results to be identical. Thus the reconstruction may add backslashes (and
nothing else) relative to the corrupted text. Exits 1 and prints the first
difference otherwise. See reports/2026-10-22--escape-corruption-audit.md.
"""

import difflib
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
    path = sys.argv[1]
    base = sys.argv[2] if len(sys.argv) > 2 else "2d144d9"
    old = subprocess.run(["git", "show", f"{base}:{path}"], capture_output=True,
                         check=True).stdout.decode("utf-8")
    new = open(path, encoding="utf-8", newline="").read()
    a = old.replace("\\", "")
    b = strip_header(new).replace("\\", "")
    if a == b:
        print(f"[PASS] {path}: differs from {base} only by backslashes")
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
