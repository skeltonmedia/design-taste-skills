---
name: taste-intake
description: Routes a taste request to setup, interview, capture, extract, or apply. Checks that taste/taste-dna.md exists first. Asks at most one question.
---

# Intake

Decide the route from the request, then follow that sub-skill's `SKILL.md`.

## First check

Look for `taste/taste-dna.md` in the project root (or the path the user names). If it is missing and the request is anything other than setup, say "No taste file yet, creating one first" and run `setup`, then continue with the original route.

## Routing

- No `taste/` folder, or the user says "set up", "start", "new client": **setup**.
- The user shares several references (URLs, screenshots, sites, type specimens) and wants their taste defined, or says "interview me", "what is my taste", "figure out what I like": **interview**.
- One new reference arrives with "save this", "log this", "add to inspiration", "I like this": **capture**.
- The user made or reports a decision ("we went with the serif", "I killed the gradient", "client rejected the comp"), or says "log this rejection", "why did I say no": **extract**.
- Design work is starting ("build a landing page", "mock up the settings screen"), or the user asks "does this fit", "review this", "is this me", "too generic?": **apply**. For new work, `apply` runs before the first render and again after.
- Two routes needed, run them in order: capture, then extract; or extract, then apply.

## The one question

Ask only if the answer changes the work:

- Interview with fewer than three pieces: "Can you add two or three more so there is something to rank?"
- Apply with no artifact or prompt provided: ask for the thing to review.
- Extract where the decision is stated but the alternatives are not: "What were the other options on the table?"

Do not ask more than one question before starting. If the user already answered it, do not ask.

## Hand-off

State the route in one line ("Reviewing the dashboard against your DNA, five-question test first"), then do the work. Do not explain the routing logic.
