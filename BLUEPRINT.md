# Blueprint: how to give an agent judgment that holds

This pack teaches an AI assistant one person's design taste. The pattern underneath is not about design. It is a way to make any agent hold a standard that belongs to a specific human, keep it current without drift, and stay honest about what it knows versus what it guessed. This file explains each part so you can rebuild it for something else: writing voice, code review standards, editorial rules, a brand, a client.

## The problem it solves

Agents forget between sessions and average between people. Telling one "be minimal" works for one reply and means something different tomorrow. Fine-tuning is expensive, opaque, and still averages. What works is a file the agent must read before acting, written in the human's own words, fed by real decisions, and guarded by rules about what may enter it.

## The six parts

### 1. One memory file that governs

`taste-dna.md` is the standard. It has a fixed shape so the agent always knows where to look and the lint can check it:

| Section | Job | Design version | Writing-voice version |
|---|---|---|---|
| 0 | The rule that wins when two others conflict | "The calendar is the interface" | "The reader's time outranks the writer's cleverness" |
| 1 | The named standard, as forces in tension, with what breaks when each is dropped | "Quiet Instrument: plain, precise, warm" | "Plain, specific, unhurried" |
| 2 | Decisions on file, dated, with what each reveals | "one accent only, 2026-04-02" | "cut the intro paragraph, 2026-03-14" |
| 3 | What gets rejected, each with a source | "confetti, 2026-05-22" | "exclamation marks in subject lines" |
| 4 | Where effort goes, and where it never goes | "spacing and type; never mascots" | "verbs and numbers; never adjectives" |
| 5 | A calibration test: five questions answerable by looking | "remove every border, does it still read?" | "read it aloud, does it sound like a person?" |
| 6 | Tensions the human has not ruled on | "dark mode warmth" | "British or American spelling" |
| 7 | Proposals waiting for the human | lines with their evidence | same |

To rebuild for another domain: keep the eight sections, rewrite the prompts in the template, write a new five-question test. The test is the part that does the work in review, so spend the time there.

### 2. An intake that routes and checks

`intake/SKILL.md` has one job before routing: confirm the memory file exists. An agent that acts without loading the standard is the failure mode this whole pattern prevents. Intake asks at most one question. Every sub-skill states its route in one line, then works.

### 3. An interview that hunts the transferable signal

People cannot list their taste. They can react. The interview (`interview/SKILL.md`) turns reactions into recorded lines by pushing each one down to something concrete, testing whether it would transfer to the person's own work, and asking what the design gave up to get it. The agent never supplies the vocabulary. The human's reached-for words go into the file.

To rebuild: keep the four moves (first contact, the specific, the transfer test, the trade). Change the objects. For writing voice, the "references" are paragraphs; for code style, they are pull requests.

### 4. An evidence bar, with marks

`references/evidence-rules.md` says what may enter the file: a decision, an artifact, or an interview answer. Everything else is marked `[inferred]` and stays visible until the human confirms or strikes it. A signal from the library needs three appearances on separate dates before it is proposed. A rejection needs one, because repeating a rejected move is the costliest mistake.

This is the part most "memory" systems skip, and it is why they drift. Without a bar, every session adds a guess and the file stops being the human's.

### 5. A tally and a proposal queue

The library (`library.md`) stores each reaction with a stable key. `tally.py` counts distinct dates per key and reports keys that cleared the bar and are not yet in the memory file. The agent writes those as proposals in section 7, with the evidence. The human promotes. Agents add to section 7; only the human moves lines out of it or edits sections 0 and 5.

That split (agents propose, human promotes) is the whole governance model. It fits in one table in `evidence-rules.md`.

### 6. A review that cites, and the smallest change

`apply/SKILL.md` runs before the first render and after. Every verdict cites the line it rests on. Failures name the element and the one change that clears them. A pass is one sentence. The review never edits the standard; anything the standard was silent on goes back through `extract` so next time it is not silent.

One rule is worth copying anywhere. Do not let the agent loop on its own critique; a critic talking to itself plateaus. The human is the loop.

## The scripts

Three small Python files with no dependencies, so the files stay usable without any agent:

- `init.py` renders the templates. Refuses to overwrite.
- `dna_lint.py` checks the memory file's shape and sourcing. Exit 1 on structural errors, so it works as a pre-commit hook.
- `tally.py` reports what cleared the bar. Reports only; never writes.

Scripts render and check. Markdown decides. If you find yourself putting a rule in a script, move it to the file the human can edit.

## Rebuilding it for something else, step by step

1. Copy `skills/taste/` to `skills/<your-domain>/`.
2. Rewrite `references/taste-dna-template.md`: same eight sections, new prompts, a new five-question test.
3. Write one invented example file the way `example-dna.md` is written. Never use a real person's file as the example.
4. Rewrite the interview's objects and the question bank. Keep the four moves.
5. Keep `evidence-rules.md` as is. It does not know about design.
6. Rewrite `review-format.md` for your output. Keep "every verdict cites a line" and "smallest change".
7. Update `check.py` fixtures. The pack is not done until its tests run from a clean clone.

## What to leave out

- Scoring the human against "best practice". The standard is theirs.
- Trend research as evidence. Context, not judgment.
- Any default taken from another person's file. One subject, one file.
- Letting the agent promote its own proposals.

Built by David Skelton, Skelton Media. MIT license.
