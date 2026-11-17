#!/usr/bin/env python3
"""Forward citations of the s=4 prior-art anchors, and download of arXiv PDFs.

Purpose: step 1 of the restricted novelty candidacy of the s=4 family
(`state/CURRENT_STATE.md`, entry «Novelty candidacy of the s=4 family
revised — 2026-11-17»). User instruction «buscalas y descargalas».

Anchors (OpenAlex work IDs, resolved by DOI on 2026-11-17):
  W2743063817  D'Ariano-Erba-Perinotti, arXiv:1708.00826 (PRA 96, 062101)
  W2004239847  D'Ariano-Perinotti, arXiv:1306.1934 (PRA 90, 062106)
  W2515088831  Arrighi-Facchini, arXiv:1609.00305 (QIC 17, 2017)

Output (this script is the provenance; nothing is screened or judged here):
  investigaciones/2026-11-17-c0-causal-body-prior-art/citas_hacia_adelante.csv
    one row per citing work: anchors cited, OpenAlex id, year, title, DOI,
    arXiv id (from OpenAlex locations), local file and SHA256 if downloaded.
  biblioteca/citas-s4-2026-11-17/<arxiv>.pdf (git-ignored local library).
  Appends missing rows to scripts/biblioteca_catalog/curated.csv with tag
  `citas-adelante-s4`, status `proposed`.

OpenAlex coverage is incomplete; a work missing here is not proven absent.
Non-arXiv works are listed but not downloaded. arXiv is queried at most
once every 3 seconds. No user or project identifiers are sent.

Usage (repo root): python3 scripts/prior_art_forward_citations.py [--no-download]
"""
import csv
import hashlib
import json
import pathlib
import re
import sys
import time
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
ANCHORS = {"W2743063817": "1708.00826", "W2004239847": "1306.1934",
           "W2515088831": "1609.00305"}
OUT_CSV = ROOT / "investigaciones/2026-11-17-c0-causal-body-prior-art/citas_hacia_adelante.csv"
LIB = ROOT / "biblioteca/citas-s4-2026-11-17"
CURATED = ROOT / "scripts/biblioteca_catalog/curated.csv"
UA = {"User-Agent": "prior-art-citation-check/1.0"}
ARX = re.compile(r"arxiv\.org/(?:abs|pdf)/([0-9]{4}\.[0-9]{4,5}|[a-z\-]+(?:\.[A-Z]{2})?/[0-9]{7})")


def get(url, tries=4):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
                return r.read()
        except Exception as exc:  # retry with backoff
            if i == tries - 1:
                raise
            time.sleep(5 * (i + 1))
            print("retry", url, exc, file=sys.stderr)


def citing(wid):
    works, cursor = [], "*"
    while cursor:
        url = (f"https://api.openalex.org/works?filter=cites:{wid}&per-page=200&cursor={cursor}"
               "&select=id,display_name,publication_year,doi,locations,ids")
        data = json.loads(get(url))
        works += data["results"]
        cursor = data["meta"].get("next_cursor")
        if not data["results"]:
            break
    return works


def arxiv_id(w):
    for loc in w.get("locations") or []:
        for k in ("landing_page_url", "pdf_url"):
            m = ARX.search(loc.get(k) or "")
            if m:
                return re.sub(r"v[0-9]+$", "", m.group(1))
    m = ARX.search(json.dumps(w.get("ids") or {}))
    return re.sub(r"v[0-9]+$", "", m.group(1)) if m else ""


def main():
    download = "--no-download" not in sys.argv
    rows = {}
    for wid, anchor in ANCHORS.items():
        for w in citing(wid):
            key = w["id"].rsplit("/", 1)[-1]
            r = rows.setdefault(key, {"openalex": key, "year": w.get("publication_year") or "",
                                      "title": (w.get("display_name") or "").replace("\n", " "),
                                      "doi": w.get("doi") or "", "arxiv": arxiv_id(w),
                                      "cites": set(), "file": "", "sha256": ""})
            r["cites"].add(anchor)
    LIB.mkdir(parents=True, exist_ok=True)
    for r in sorted(rows.values(), key=lambda r: (str(r["year"]), r["title"])):
        if not (download and r["arxiv"]):
            continue
        dest = LIB / (r["arxiv"].replace("/", "_") + ".pdf")
        if not dest.exists():
            time.sleep(3)
            try:
                data = get(f"https://arxiv.org/pdf/{r['arxiv']}")
            except Exception as exc:
                print("download failed", r["arxiv"], exc, file=sys.stderr)
                continue
            if not data.startswith(b"%PDF"):
                print("not a PDF", r["arxiv"], file=sys.stderr)
                continue
            dest.write_bytes(data)
        r["file"] = str(dest.relative_to(ROOT))
        r["sha256"] = hashlib.sha256(dest.read_bytes()).hexdigest()
    with OUT_CSV.open("w", newline="") as f:
        wr = csv.writer(f)
        wr.writerow(["cites", "openalex", "year", "title", "doi", "arxiv", "file", "sha256"])
        for r in sorted(rows.values(), key=lambda r: (str(r["year"]), r["title"])):
            wr.writerow([";".join(sorted(r["cites"])), r["openalex"], r["year"], r["title"],
                         r["doi"], r["arxiv"], r["file"], r["sha256"]])
    existing = {row.split(",", 1)[0] for row in CURATED.read_text().splitlines()
                if row and not row.startswith("#")}
    added = 0
    with CURATED.open("a", newline="") as f:
        wr = csv.writer(f)
        for r in sorted(rows.values(), key=lambda r: r["openalex"]):
            if not r["file"]:
                continue
            path = r["file"].split("biblioteca/", 1)[1]
            if path in existing:
                continue
            wr.writerow([path, "", "citas-adelante-s4",
                         "forward citation of arXiv:" + "+".join(sorted(r["cites"]))
                         + " (OpenAlex, 2026-11-17)", "proposed"])
            added += 1
    n_arx = sum(1 for r in rows.values() if r["arxiv"])
    n_dl = sum(1 for r in rows.values() if r["file"])
    print(json.dumps({"citing_works": len(rows), "with_arxiv": n_arx, "downloaded": n_dl,
                      "curated_rows_added": added,
                      "per_anchor": {a: sum(1 for r in rows.values() if a in r["cites"])
                                     for a in ANCHORS.values()}}, indent=2))


if __name__ == "__main__":
    main()
