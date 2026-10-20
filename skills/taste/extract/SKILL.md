---
name: taste-extract
description: Turns a real design decision or rejection into recorded judgment. Writes a rejection log entry, or a candidate DNA line under Proposed with the decision that produced it. Promotes a tallied signal into a proposal. Never edits a ratified DNA line from one event.
---

# Extract

Taste is legible in choices, not adjectives. This sub-skill writes the choice down the same session it happens, so the DNA stays current because decisions feed it, not because someone polishes it later.

Three inputs, three outputs.

## 1. A rejection

Trigger: the user declined something, or reports a client did. "Killed the gradient." "Went with the plain wordmark, the clever ones lost."

1. Get the alternatives if not stated (one question, from intake).
2. Append to `taste/rejections.md` (format in `references/library-format.md`): date, what was declined, what was chosen instead, the user's stated reason verbatim, and one line on what the no reveals, marked `[inferred]` if the user did not say it.
3. If the reveal line matches an existing bullet in DNA section 3 (What gets rejected), add the date as a second source on that bullet. If it is new, add it under Proposed, section 7.

## 2. A decision

Trigger: the user chose something, with or without rejections. "Kept the condensed face on the scoreboard even though the brand says otherwise."

1. Add a row to DNA section 2 (Decisions): the decision, the date, and what it reveals. The reveal is one sentence. If the user stated the reason, it is their sentence. If you inferred it, mark `[inferred]`.
2. If the decision breaks an existing DNA line, do not edit the line. Add the conflict to section 6 (Known tensions) as a question with both sources.
3. Run `dna_lint.py`. Fix anything structural before finishing.

## 3. A tallied signal

Trigger: `tally.py` reports a key with three or more appearances across separate sessions that is not yet in the DNA.

1. Read the three library rows. Write one candidate line in the subject's words, under section 7 (Proposed), with the three dates and the key.
2. Say which section it would belong in once promoted (1, 3, 4, or 5) and why.
3. Do not promote it. The user moves it out of Proposed. Promotion is theirs.

## Evidence rules

Load `references/evidence-rules.md` when unsure. The short version: every line traces to a decision, an artifact, or an interview answer; inferences carry the `[inferred]` mark; the governing rule and the calibration test change only by the user's explicit decision; nothing is deleted, struck lines stay struck with the date.

## Output

End with the exact lines added, where, and the lint result. No summary of the method.
