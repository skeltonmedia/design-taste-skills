---
name: taste-apply
description: Reviews a design, mockup, page, prompt, or plan against the recorded DNA before and after rendering. Names the DNA lines honored or broken, runs the calibration test, and proposes the smallest change. Never rewrites the DNA from one review.
---

# Apply

The DNA governs; this sub-skill holds the work to it. It runs twice on new work: once on the plan or prompt before the first render, once on the result.

## Before rendering

1. Load `taste/taste-dna.md`. Read section 0 (governing rule), 1 (named aesthetic), 3 (rejections), and 5 (calibration test). Skip the rest unless the task touches it.
2. Restate the plan in three lines: what the work is, which DNA lines it leans on, which rejected moves it is at risk of making. A plan that cannot name a single DNA line is generic; stop and ask what the piece is for.
3. If a brand system or client design system applies, it stays authoritative for tokens (type, color, spacing). The DNA supplies judgment inside those tokens. Where the two collide, say so and log it under Known tensions; do not pick silently.
4. If the user has approved an outside reference (a site to borrow from), name what is borrowed, what is adapted, and what is avoided before implementing. Approval to look is not approval to copy.

## After rendering

Run the calibration test from section 5, one verdict per question, each citing the DNA line it rests on. Then:

- List every section 3 rejection the work commits, with the element that commits it.
- Propose the smallest change that clears the failures. One change per failure. No redesign.
- If the work passes all five and breaks no rejection, say so in one line and stop. Do not pad a pass with suggestions.

Output in the format from `references/review-format.md`.

## When the DNA is silent

A decision the DNA does not cover is not a license to guess. Make the call the way the governing rule points, say that the DNA was silent, and hand the decision to `extract` so it gets recorded. Next time the DNA will not be silent.

## When the DNA is empty

A fresh file with every section `TODO` cannot govern. Say so, run the work on the user's stated brief alone, and recommend an interview on three to five references before the next piece. Do not fill the DNA from the review.

## Do not

- Do not score the work against trends, awards, or "best practice". Those are context, not the standard.
- Do not run more than one review loop without the user in it. A critic talking to itself plateaus; the user's eye is the loop.
- Do not soften a failed question. "Fails 1: remove the card borders and the three columns collapse into one column of text" is the useful sentence.
