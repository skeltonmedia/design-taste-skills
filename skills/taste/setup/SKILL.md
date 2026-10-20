---
name: taste-setup
description: Creates the taste/ folder in a project with a blank DNA file, inspiration library, rejection log, and inbox. Run once per person or client. Never overwrites an existing file.
---

# Setup

Creates the memory the other sub-skills read and write.

## Steps

1. Ask for the subject name if it was not given: the person, team, or client whose taste this file records. One file per subject.
2. Run the script from the project root:

```bash
python3 <pack>/skills/taste/setup/scripts/init.py --subject "<name>" [--dir taste]
```

   It creates `taste/taste-dna.md`, `taste/library.md`, `taste/rejections.md`, and `taste/inbox/`. It refuses to overwrite anything that exists.

3. Open the new `taste-dna.md` and fill section 0 (the governing rule) only if the user already stated one. Otherwise leave every `TODO` in place. A blank DNA is honest; a guessed one is not.
4. Tell the user the three ways the file fills up, in one line each: interview a batch of inspiration, log decisions and rejections as they happen, capture single pieces.

## For a client

Use `--dir clients/<client>/taste` so client files stay separate. Do not copy any line from another subject's DNA into the client file, including the calibration test. The client's five questions come from their own interview.

## What a fresh file looks like

Every section present, every body a `TODO` with a one-line prompt of what belongs there. `dna_lint.py` passes a fresh file structurally and reports the unfilled sections as warnings, so the file can be committed on day one.
