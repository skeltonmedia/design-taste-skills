#!/usr/bin/env python3
"""Create a taste/ folder for one subject from the pack templates.

    python3 init.py --subject "Harbor" [--dir taste] [--date 2026-01-01]

Writes taste-dna.md, library.md, rejections.md and inbox/. Refuses to
overwrite any file that already exists."""
import argparse
import datetime as dt
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REFS = HERE.parent.parent / "references"
TEMPLATES = {
    "taste-dna.md": REFS / "taste-dna-template.md",
    "library.md": REFS / "library-template.md",
    "rejections.md": REFS / "rejections-template.md",
}


def render(template: Path, subject: str, date: str) -> str:
    text = template.read_text(encoding="utf-8")
    return text.replace("{{SUBJECT}}", subject).replace("{{DATE}}", date)


def init(target: Path, subject: str, date: str) -> list[Path]:
    existing = [target / name for name in TEMPLATES if (target / name).exists()]
    if existing:
        raise FileExistsError(", ".join(str(p) for p in existing))
    target.mkdir(parents=True, exist_ok=True)
    (target / "inbox").mkdir(exist_ok=True)
    (target / "inbox" / "drops.md").write_text(
        f"# Inbox: {subject}\n\nRaw drops, one per line. Cleared by the next interview session.\n",
        encoding="utf-8",
    )
    written = []
    for name, template in TEMPLATES.items():
        path = target / name
        path.write_text(render(template, subject, date), encoding="utf-8")
        written.append(path)
    written.append(target / "inbox" / "drops.md")
    return written


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--subject", required=True, help="person, team, or client the file records")
    ap.add_argument("--dir", default="taste", help="folder to create (default: taste)")
    ap.add_argument("--date", default=dt.date.today().isoformat(), help="created date, YYYY-MM-DD")
    args = ap.parse_args(argv)
    try:
        written = init(Path(args.dir), args.subject.strip(), args.date)
    except FileExistsError as e:
        print(f"refusing to overwrite: {e}", file=sys.stderr)
        return 1
    for p in written:
        print("wrote", p)
    print("next: interview three to five references, or log the first rejection")
    return 0


if __name__ == "__main__":
    sys.exit(main())
