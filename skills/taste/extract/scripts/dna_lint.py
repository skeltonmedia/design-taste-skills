#!/usr/bin/env python3
"""Lint a taste-dna.md for structure and sourcing.

    python3 dna_lint.py taste/taste-dna.md [--json]

Errors (exit 1): missing frontmatter or subject, a missing section 0 to 7,
a decision row without a date, a rejection bullet without a source, a
calibration test that is not exactly five questions.
Warnings (exit 0): unfilled TODO sections. Info: lines still marked [inferred]."""
import json
import re
import sys
from pathlib import Path

SECTIONS = {
    0: "governing rule",
    1: "named aesthetic",
    2: "decisions",
    3: "rejections",
    4: "appetite",
    5: "calibration test",
    6: "known tensions",
    7: "proposed",
}
HEADING = re.compile(r"^## (\d)\.")
DATE = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
SOURCE = re.compile(r"\(source:|\[inferred\]|rejections\.md", re.IGNORECASE)
QUESTION = re.compile(r"^\d+\.\s+\S")


def split_sections(lines):
    """Return {section_number: [(lineno, text), ...]} for '## N.' headings."""
    out, current = {}, None
    for i, line in enumerate(lines, 1):
        m = HEADING.match(line)
        if m:
            current = int(m.group(1))
            out[current] = []
            continue
        if current is not None:
            out[current].append((i, line))
    return out


def table_rows(block):
    rows = []
    for lineno, line in block:
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if not cells or set(cells[0]) <= {"-", ":", ""} or cells[0].lower() == "decision":
            continue
        rows.append((lineno, cells))
    return rows


def lint(text: str):
    findings = []

    def add(level, code, line, msg):
        findings.append({"level": level, "code": code, "line": line, "msg": msg})

    lines = text.splitlines()
    if not text.startswith("---"):
        add("error", "no-frontmatter", 1, "file must start with frontmatter")
    else:
        fm = text.split("---", 2)[1]
        if not re.search(r"^subject:\s*\S", fm, re.MULTILINE):
            add("error", "no-subject", 1, "frontmatter lacks subject:")

    sections = split_sections(lines)
    for n, name in SECTIONS.items():
        if n not in sections:
            add("error", "missing-section", 0, f"section {n} ({name}) missing")

    for n, block in sections.items():
        body = "\n".join(t for _, t in block)
        if "TODO" in body:
            add("warn", "unfilled", block[0][0] if block else 0, f"section {n} ({SECTIONS.get(n, '?')}) has TODO")

    for lineno, cells in table_rows(sections.get(2, [])):
        if len(cells) < 3:
            add("error", "decision-columns", lineno, "decision row needs decision | date | what it reveals")
            continue
        date = cells[1]
        if date == "TODO":
            continue
        if not (DATE.search(date) or date.lower() == "canonical"):
            add("error", "undated-decision", lineno, f"decision row has no date: {cells[0][:50]}")

    for lineno, line in sections.get(3, []):
        s = line.strip()
        if not s.startswith("-") or "TODO" in s:
            continue
        if not (SOURCE.search(s) or DATE.search(s)):
            add("error", "unsourced-rejection", lineno, f"rejection has no source: {s[:60]}")

    questions = [t for _, t in sections.get(5, []) if QUESTION.match(t.strip())]
    if 5 in sections and len(questions) != 5:
        add("error", "calibration-count", sections[5][0][0] if sections[5] else 0, f"calibration test has {len(questions)} questions, needs 5")

    for i, line in enumerate(lines, 1):
        # A backticked `[inferred]` is prose explaining the mark, not a marked line.
        if "[inferred]" in line.replace("`[inferred]`", ""):
            add("info", "inferred", i, line.strip()[:70])

    return findings


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    path = Path(argv[0])
    findings = lint(path.read_text(encoding="utf-8"))
    if "--json" in argv:
        print(json.dumps(findings, indent=2))
    else:
        for f in findings:
            loc = f"line {f['line']}" if f["line"] else "file"
            print(f"{f['level'].upper():5} {f['code']} ({loc}): {f['msg']}")
        errors = sum(1 for f in findings if f["level"] == "error")
        warns = sum(1 for f in findings if f["level"] == "warn")
        inferred = sum(1 for f in findings if f["code"] == "inferred")
        print(f"{errors} error(s), {warns} unfilled section(s), {inferred} inferred line(s) awaiting confirmation")
    return 1 if any(f["level"] == "error" for f in findings) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
