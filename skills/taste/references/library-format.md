# Library and rejection log formats

Two files in `taste/`. Both are plain markdown so the subject can edit them by hand and the scripts can still read them.

## `library.md`

One table. Nothing enters it without an interview pass (full or the two-question short loop in `capture`).

```
| Date | Piece / source | Gut rank | Signal (subject's words) | Key | Flags |
|---|---|---|---|---|---|
| 2026-04-09 | invoice app, pricing page (url) | 1 of 5 | "the numbers line up before anything else does" | tabular-figures | |
| 2026-04-09 | agency site (url) | 5 of 5 | "it's all hero, no work" | hero-over-work | declined |
```

Columns:

- **Date**: the session date. The tally counts distinct dates per key, so a batch interviewed on one day counts once.
- **Piece / source**: enough to find it again. A URL, a file name, a screenshot path.
- **Gut rank**: position in the session's ten-second ranking, `declined` for a rejection, blank for a single capture with no ranking.
- **Signal**: the subject's words, quoted. Not a description of the piece. Not the agent's vocabulary.
- **Key**: kebab-case, names the move, not the piece. Reuse an existing key when the same move appears again; `tally.py --keys` lists what exists. Invent a new key only when the move is new.
- **Flags**: `declined`, `[aspiration]`, `client`, or blank.

Below the table, a session log, newest last:

```
## Session 2026-04-09

Pieces: 5. Raw rank: C, A, E, B, D.
Shares: "the top two let the content be the layout"
Embarrassed to ship: D, "it's all hero, no work"
```

## `rejections.md`

One entry per no, newest last. A rejection enters here the day it happens; it does not wait for the three-appearance bar.

```
## 2026-05-30: landing page comp with centered hero and three feature cards

- Chosen instead: the product's week view as the first screen, one sentence above it
- Reason (verbatim): "that's every SaaS page on earth, nobody would know it was ours"
- Reveals: distinction comes from the product shown, not the page composition [inferred]
- DNA: section 3, "Generic SaaS composition"
```

Fields:

- **Chosen instead**: the alternative that won, or "nothing yet".
- **Reason (verbatim)**: the subject's sentence. If they did not give one, write "not stated" and mark the Reveals line `[inferred]`.
- **Reveals**: one line, the transferable signal.
- **DNA**: the section 3 bullet it supports, or "proposed" if it is new.

## `inbox/`

Raw drops, no format. A `drops.md` with one line per item, or files. Cleared by the next interview session.
