# Design Taste Skills

Make your AI assistant design like you, not like every other AI.

Free, open, and written for designers who are new to working with AI agents. If you have noticed that everything the AI makes looks the same, this is the fix. It is also a blueprint: the same pattern works for any kind of judgment you want an agent to hold. See `BLUEPRINT.md`.

## The idea in one paragraph

An AI assistant has no taste of its own. It has an average of everyone's. The only way to get your taste out of it is to write your taste down in a form the assistant reads before it works, and to keep that file current as you make decisions. Taste is not a mood board. It is recorded judgment: what you chose, what you declined, and why. This pack gives you the file, the interview that fills it, the log that keeps it honest, and the review that holds the AI to it.

## What you get

Six small skills in one folder. A skill is a markdown file with instructions the assistant follows when a request matches. These run in Claude Code, Codex, Cursor, and anything else that reads `SKILL.md` files.

| Skill | What it does | When you use it |
|---|---|---|
| `setup` | Creates a `taste/` folder in your project with four files | Once, at the start |
| `interview` | Asks you about three to seven references and writes down what you reacted to, in your words | First week, then whenever you have a batch |
| `capture` | Files one new reference with the signal it carries | Any time you see something you like |
| `extract` | Writes a decision or a rejection into the taste file | Every time you choose or decline something |
| `apply` | Reviews a design or a prompt against your taste file and names the smallest change | Before and after every piece of design work |
| `intake` | Routes your request to the right one | Automatic |

## Install (five minutes)

1. Clone this repo.

```bash
git clone https://github.com/skeltonmedia/design-taste-skills
```

2. Copy the skill folder where your assistant looks for skills.

   - Claude Code, for every project: `cp -r design-taste-skills/skills/taste ~/.claude/skills/`
   - Claude Code, one project: copy the same folder to `.claude/skills/` inside the project.
   - Codex or Cursor: copy the folder into the project and add a line to `AGENTS.md` pointing at `skills/taste/SKILL.md`.

3. In your project, create the taste folder.

```bash
python3 ~/.claude/skills/taste/setup/scripts/init.py --subject "Your name or studio"
```

4. Ask the assistant: "interview me on these five sites" and paste five links. Answer its questions. That is the whole setup.

## What the first week looks like

- **Day 1.** Interview on five references. The assistant asks what you noticed first, what specifically is doing it, whether the move would transfer to your work, and what the design gave up to get it. It writes your answers into `taste/library.md` in your words.
- **Day 2 to 5.** Work as normal. Each time you make a call ("no gradients", "keep the big clock"), say "log that". The assistant writes it to `taste/taste-dna.md` or `taste/rejections.md` with the date.
- **Before any design task.** Say "review the plan against my taste first". The assistant reads the taste file, says which lines the plan leans on and which rejections it risks, and then builds.
- **After.** "Does this pass?" It runs your five-question calibration test and names the smallest change.
- **End of week.** Run the tally. Any signal that showed up three times gets proposed as a new line in your file. You promote it or strike it.

## The four files in `taste/`

| File | Holds | Who writes it |
|---|---|---|
| `taste-dna.md` | The judgment: governing rule, named aesthetic, decisions, rejections, appetite, calibration test, open tensions, proposals | the assistant proposes, you promote |
| `library.md` | References you reacted to, with the signal each one carries and a short key for tallying | interview, capture |
| `rejections.md` | Everything you said no to, with the alternative and the reason | extract |
| `inbox/` | Raw links you have not reacted to yet | you |

A filled file, for a made-up studio, is in `skills/taste/references/example-dna.md`. Read it once; it shows what "written down" looks like.

## Why rejections

A taste is defined by its no. Seven declined logo options say more about a designer than any list of adjectives. The rejection log is the file most people never keep, and it is the one that stops the assistant making the same mistake twice.

## How the learning works

There is no model training and nothing is sent anywhere. The memory is the markdown in `taste/`. Every design session starts by loading it. A signal seen three times across separate sessions clears the evidence bar and gets proposed. Inferences the assistant makes are marked `[inferred]` until you confirm them. Nothing enters the file without a decision, an artifact, or an interview answer behind it. The rules are in `skills/taste/references/evidence-rules.md`.

## Two scripts that run without an assistant

```bash
python3 skills/taste/extract/scripts/dna_lint.py taste/taste-dna.md
python3 skills/taste/capture/scripts/tally.py taste/library.md taste/taste-dna.md
```

The first checks your taste file has every section, that decisions carry dates, that rejections carry sources, and lists what is still `[inferred]`. Exit code 1 on structural errors, so it works as a pre-commit check. The second lists the signals that have cleared the three-appearance bar and are not yet in the file.

## Test the pack

```bash
python3 skills/taste/testing/check.py
```

## What it will not do

It does not grade your taste against "good design" or against trends. Your taste is the standard; the pack records it and holds the assistant to it. It does not invent preferences. It does not run a critic loop on its own; you are the loop.

## Use it as a blueprint

The pattern (memory files, an evidence bar, a tally, proposals the human promotes) is not specific to design. `BLUEPRINT.md` explains each part and how to rebuild it for writing voice, code style, editorial standards, or anything else you want an agent to hold steady.

MIT license. Built by David Skelton, Skelton Media. Questions and pull requests welcome.
