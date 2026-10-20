---
name: taste-capture
description: Files one new piece of inspiration to the library with its extracted signal and a stable key, then reports whether any signal has cleared the three-appearance bar. For a batch of three or more, use interview instead.
---

# Capture

One piece, one row, one short interview pass. Nothing enters the library without a signal; a bare link is a drop for the inbox, not a capture.

## Steps

1. If the user gave only a link or image with no reaction, run the two-question short loop:
   - "What did you notice first?"
   - "What specifically is doing that?"
   Stop there. A single capture does not need the transfer test; the tally will tell us if it matters.
2. Write the row to `taste/library.md` in the format from `references/library-format.md`:
   - Date (today), piece and source, gut rank if given (else blank), the signal in their words, a kebab-case key, flags.
   - The key is the stable name of the signal, not the piece. Reuse an existing key when the signal is the same move seen again. Run `tally.py --keys` to list the keys already in use before inventing one.
3. If the user reacted negatively, the row still goes in the library with gut rank `declined`, and the reason goes to `taste/rejections.md` via `extract`.
4. Run the tally:

```bash
python3 <pack>/skills/taste/capture/scripts/tally.py taste/library.md taste/taste-dna.md
```

5. If a key is reported ready, hand off to `extract` to write the proposal. Do not write it yourself from a single capture.

## Inbox

Raw drops the user has not reacted to go in `taste/inbox/` as a file or a line in `taste/inbox/drops.md`, and are cleared by the next interview session. Do not interview the user on an inbox item they did not ask about; batch them.

## Do not

- Do not describe the piece in your own design vocabulary. The signal cell holds their words.
- Do not tag the piece with a brand or palette verdict. The library serves every project; judgment about fit happens in `apply`.
