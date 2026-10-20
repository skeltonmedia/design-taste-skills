---
name: taste-interview
description: Runs a taste interview on a person or client against a batch of three to seven inspiration pieces. Hunts the specific, transferable signal in the subject's own words, files each piece to the library, and proposes DNA lines only when the evidence bar is met.
---

# Interview

You are not asking "do you like this?" Like and dislike are mood. You are hunting the specific, transferable signal: the thing that would still be true about a different artifact. "I like this site" is nothing. "The nav disappears and the work is the interface" is a DNA line.

Never lead. Never supply the vocabulary first. Let the subject reach for their own words, then reflect them back sharpened. Their reached-for words are worth ten of yours. Load `references/interview-questions.md` for the full bank; the core loop is below.

## Session shape (3 to 7 pieces)

1. **Gut rank.** "Ranked gut call, ten seconds each, before we talk." Record the raw order. Do not discuss yet.
2. **Per-piece loop** on the top two and the bottom one. The bottom pick matters most; rejections are the sharpest signal.
3. **Synthesis**, two questions:
   - "What do your top picks share that your bottom pick lacks?" This is their theory of their own taste.
   - "Which of these would you be embarrassed to have shipped?" This is the taste floor.

## Per-piece loop (about four exchanges)

1. **First contact.** Open the piece. Ask only: "What did you notice first?" Where the eye goes reveals more than an opinion.
2. **The specific.** Whatever they praise or reject, push one level down: "What specifically is doing that?" Keep going until the answer names something concrete: a spacing rhythm, a type weight, a color's job, an absence.
3. **The transfer test.** "If we stole only that one move for your work, what would it touch?" A signal that transfers is taste. One that does not is context.
4. **The trade.** "What did this design give up to get that?" If they can name the cost, the appetite is informed. If not, mark the signal `[aspiration]` and note what acquiring it would cost (a tool, a skill, a hire).

Run one exchange at a time. Wait for the answer. Do not stack questions.

## After the session

1. File each piece to `taste/library.md` (format in `references/library-format.md`): date, piece, gut rank, the signal in their words, a kebab-case key for the signal, flags.
2. Run `tally.py`. A key seen in three separate sessions clears the evidence bar. Propose it under the DNA's Proposed section, citing the three rows. One appearance is a data point; three is taste.
3. A signal that contradicts an existing DNA line goes to Known tensions as a question, never a silent edit. Taste moves; the file records the movement.
4. Append a dated session entry to the bottom of `library.md`: pieces, raw rank, the two synthesis answers verbatim.

## Client variant

Differences only:

- Open with an artifact pull: their current site, deck, or product plus two or three competitors, reviewed with the same loop before any new inspiration. Where they are reads differently from where they want to be, and the gap is the engagement.
- Add: "Show me the competitor that makes you angry." Envy is taste data.
- Add: "What have you rejected before: an agency comp, a rebrand, a template?" If they have the artifacts, file them to `rejections.md`.
- Output is the client's own `taste-dna.md`, from the blank template. No other subject's DNA is a default.
