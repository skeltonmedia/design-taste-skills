---
name: taste
description: Make an AI assistant design like one specific person or team, not like generic AI. Record design judgment as a DNA file (governing rule, named aesthetic, decisions, rejections, appetite, calibration test); run a taste interview on a person or client against inspiration; log rejections; extract DNA lines from real decisions; review any design, mockup, page, or prompt against the DNA before rendering. Use when starting any visual work, when someone asks "does this fit my taste" or "why does everything the AI makes look the same", when new inspiration lands, when a design gets declined, or when a client engagement starts.
version: 0.1.0
---

# Taste

Product index. Read `intake/SKILL.md` first; it routes the request to one of five sub-skills.

| Sub-skill | Use when | Returns |
|---|---|---|
| `setup/` | The project has no `taste/` folder yet | The folder with a blank DNA, library, rejection log, inbox |
| `interview/` | The user wants their taste (or a client's) defined from inspiration | Library rows in their words, candidate DNA lines, a session log |
| `capture/` | One new piece of inspiration arrives | One library row with a keyed signal, the updated tally |
| `extract/` | A design decision or rejection just happened | A candidate DNA line under Proposed, or a rejection log entry |
| `apply/` | Any design work is about to start or be judged | A review citing DNA lines, and the smallest change |

Where the memory lives, in the user's project:

- `taste/taste-dna.md`: the judgment. Template in `references/taste-dna-template.md`, worked example in `references/example-dna.md`.
- `taste/library.md`: interviewed inspiration with keyed signals. Format in `references/library-format.md`.
- `taste/rejections.md`: everything declined and what the no reveals. Same reference.
- `taste/inbox/`: raw drops waiting for an interview pass.

Shared references, loaded only when a sub-skill asks for them:

- `references/evidence-rules.md`: what may enter the DNA and how it is marked.
- `references/interview-questions.md`: the question bank.
- `references/review-format.md`: the output shape for `apply`.

Rules that apply to every sub-skill:

1. Load `taste/taste-dna.md` before any visual work. If it does not exist, route to `setup` and say so in one line.
2. Never invent a preference. Every DNA line traces to a decision, an artifact, or an interview answer. Inferences are marked `[inferred]` until the user confirms them.
3. The user's words are the data. Reflect them back sharpened; do not replace them with design vocabulary they did not reach for.
4. Taste is the standard, never the thing judged. Do not score the user's taste against "good design" or against trends.
5. A conflict between new evidence and the recorded DNA is surfaced as a question under Known tensions, never resolved silently.
6. One person's DNA is never a default for another person or client. A client gets their own file from their own interview.
