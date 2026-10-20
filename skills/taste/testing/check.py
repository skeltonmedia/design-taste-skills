#!/usr/bin/env python3
"""Pack self-test. Run: python3 skills/taste/testing/check.py

Checks: every SKILL.md has frontmatter and stays under 500 lines; required
references exist; the example DNA passes the lint; the broken fixture fails
with the expected codes; the tally reports the expected keys; init.py
creates a folder whose fresh DNA passes the lint structurally; the pack's
own prose carries no em dashes and none of a short banned-word list."""
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

PACK = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PACK / "extract" / "scripts"))
sys.path.insert(0, str(PACK / "capture" / "scripts"))
from dna_lint import lint  # noqa: E402
from tally import tally  # noqa: E402

FIXTURES = PACK / "testing" / "fixtures"
EXPECTED = json.loads((FIXTURES / "expected.json").read_text(encoding="utf-8"))
REQUIRED_REFS = [
    "references/taste-dna-template.md",
    "references/example-dna.md",
    "references/evidence-rules.md",
    "references/interview-questions.md",
    "references/review-format.md",
    "references/library-format.md",
    "references/library-template.md",
    "references/rejections-template.md",
]
BANNED = ["delve", "leverage", "robust", "elevate", "empower", "streamline", "seamless", "unlock", "supercharge", "game changer"]


def check_skill_files():
    errors = []
    for skill in PACK.rglob("SKILL.md"):
        text = skill.read_text(encoding="utf-8")
        rel = skill.relative_to(PACK)
        if not text.startswith("---"):
            errors.append(f"{rel}: missing frontmatter")
            continue
        fm = text.split("---", 2)[1]
        for field in ("name:", "description:"):
            if not re.search(rf"^{field}", fm, re.MULTILINE):
                errors.append(f"{rel}: frontmatter lacks {field}")
        if text.count("\n") > 500:
            errors.append(f"{rel}: over 500 lines")
    return errors


def check_refs():
    return [f"missing {r}" for r in REQUIRED_REFS if not (PACK / r).exists()]


def check_lint():
    errors = []
    good = lint((PACK / "references" / "example-dna.md").read_text(encoding="utf-8"))
    bad_levels = [f for f in good if f["level"] == "error"]
    if bad_levels:
        errors.append(f"example-dna: unexpected errors {bad_levels}")
    if not any(f["code"] == "inferred" for f in good):
        errors.append("example-dna: expected at least one [inferred] line to report")
    bad = lint((FIXTURES / "bad-dna.md").read_text(encoding="utf-8"))
    codes = {f["code"] for f in bad if f["level"] == "error"}
    for code in EXPECTED["bad_dna_error_codes"]:
        if code not in codes:
            errors.append(f"bad-dna: expected error '{code}' not raised")
    missing = [f for f in bad if f["code"] == "missing-section"]
    if not any(f"section {EXPECTED['bad_dna_missing_section']} " in f["msg"] for f in missing):
        errors.append(f"bad-dna: section {EXPECTED['bad_dna_missing_section']} should be reported missing")
    return errors


def check_tally():
    errors = []
    library = (FIXTURES / "library-sample.md").read_text(encoding="utf-8")
    dna = (PACK / "references" / "example-dna.md").read_text(encoding="utf-8")
    want = EXPECTED["tally_against_example_dna"]
    got = tally(library, dna)
    if got["ready"] != want["ready"]:
        errors.append(f"tally ready: got {got['ready']}, want {want['ready']}")
    if got["counts"] != want["counts"]:
        errors.append(f"tally counts: got {got['counts']}, want {want['counts']}")
    if got["in_dna"] != want["in_dna"]:
        errors.append(f"tally in_dna: got {got['in_dna']}, want {want['in_dna']}")
    bare = tally(library)
    if bare["ready"] != EXPECTED["tally_without_dna_ready"]:
        errors.append(f"tally without dna: got {bare['ready']}")
    return errors


def check_init():
    errors = []
    with tempfile.TemporaryDirectory() as tmp:
        target = Path(tmp) / "taste"
        cmd = [sys.executable, str(PACK / "setup" / "scripts" / "init.py"), "--subject", "Fixture Subject", "--dir", str(target), "--date", "2026-01-01"]
        run = subprocess.run(cmd, capture_output=True, text=True)
        if run.returncode != 0:
            errors.append(f"init.py failed: {run.stderr.strip()}")
            return errors
        for name in ("taste-dna.md", "library.md", "rejections.md", "inbox/drops.md"):
            if not (target / name).exists():
                errors.append(f"init.py did not create {name}")
        fresh = (target / "taste-dna.md").read_text(encoding="utf-8")
        if "{{" in fresh:
            errors.append("init.py left a placeholder unrendered")
        if "Fixture Subject" not in fresh:
            errors.append("init.py did not render the subject")
        findings = lint(fresh)
        if any(f["level"] == "error" for f in findings):
            errors.append(f"fresh DNA has structural errors: {[f['code'] for f in findings if f['level'] == 'error']}")
        if not any(f["code"] == "unfilled" for f in findings):
            errors.append("fresh DNA should report unfilled sections")
        rerun = subprocess.run(cmd, capture_output=True, text=True)
        if rerun.returncode == 0:
            errors.append("init.py overwrote existing files on a second run")
    return errors


def check_own_prose():
    errors = []
    root = PACK.parent.parent
    targets = [root / "README.md", root / "BLUEPRINT.md", root / "CHANGELOG.md"] + sorted(PACK.rglob("*.md"))
    for path in targets:
        if not path.exists() or "fixtures" in path.parts:
            continue
        rel = path.relative_to(root)
        text = path.read_text(encoding="utf-8")
        for i, line in enumerate(text.splitlines(), 1):
            if "—" in line:
                errors.append(f"{rel}: em dash line {i}")
            low = line.lower()
            for word in BANNED:
                if re.search(rf"\b{re.escape(word)}\b", low):
                    errors.append(f"{rel}: banned word '{word}' line {i}")
    return errors


def main():
    errors = check_skill_files() + check_refs() + check_lint() + check_tally() + check_init() + check_own_prose()
    for e in errors:
        print("FAIL", e)
    print("ok" if not errors else f"{len(errors)} failure(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
