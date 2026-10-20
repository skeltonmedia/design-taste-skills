#!/usr/bin/env python3
"""Tally library signals toward the three-appearance bar.

    python3 tally.py taste/library.md [taste/taste-dna.md] [--keys] [--json] [--bar 3]

A key is ready when it appears on at least --bar distinct session dates and
the DNA file (if given) does not already mention it. --keys lists every key
with its count, for reuse before inventing a new one. Exit code is always 0;
this script reports, it does not gate."""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
KEY = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def parse_rows(text: str):
    """Yield (date, key, flags) for every data row of the library table."""
    header = None
    for line in text.splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if header is None:
            lowered = [c.lower() for c in cells]
            if "key" in lowered and "date" in lowered:
                header = {name: i for i, name in enumerate(lowered)}
            continue
        if set(cells[0]) <= {"-", ":", ""}:
            continue
        try:
            date = cells[header["date"]]
            key = cells[header["key"]]
        except IndexError:
            continue
        flags = cells[header["flags"]] if "flags" in header and header["flags"] < len(cells) else ""
        if DATE.match(date) and KEY.match(key):
            yield date, key, flags


def tally(library_text: str, dna_text: str = "", bar: int = 3):
    dates = defaultdict(set)
    flags = defaultdict(set)
    for date, key, flag in parse_rows(library_text):
        dates[key].add(date)
        if flag:
            flags[key].add(flag)
    counts = {k: len(v) for k, v in dates.items()}
    in_dna = {k for k in counts if k in dna_text}
    ready = sorted(k for k, n in counts.items() if n >= bar and k not in in_dna)
    return {
        "counts": dict(sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))),
        "dates": {k: sorted(v) for k, v in dates.items()},
        "flags": {k: sorted(v) for k, v in flags.items()},
        "in_dna": sorted(in_dna),
        "ready": ready,
        "bar": bar,
    }


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    paths = [a for a in argv if not a.startswith("--") and not a.isdigit()]
    bar = 3
    if "--bar" in argv:
        bar = int(argv[argv.index("--bar") + 1])
        paths = [p for p in paths if p != str(bar)]
    library = Path(paths[0]).read_text(encoding="utf-8")
    dna = Path(paths[1]).read_text(encoding="utf-8") if len(paths) > 1 else ""
    result = tally(library, dna, bar)
    if "--json" in argv:
        print(json.dumps(result, indent=2))
        return 0
    if "--keys" in argv:
        for k, n in result["counts"].items():
            mark = " (in DNA)" if k in result["in_dna"] else ""
            print(f"{n:2}  {k}{mark}")
        return 0
    if not result["ready"]:
        print(f"nothing ready: no key on {bar}+ session dates outside the DNA")
    for k in result["ready"]:
        print(f"READY {k}: {', '.join(result['dates'][k])}  -> write a proposal (extract)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
