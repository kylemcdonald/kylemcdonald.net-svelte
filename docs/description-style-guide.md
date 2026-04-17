# Description Style Guide

Basis for this guide:

- Home page copy in [`src/routes/+page.svelte`](../src/routes/+page.svelte)
- 76 project entries in [`src/routes/projects.json`](../src/routes/projects.json)
- Snapshot analyzed on 2026-04-16

## Corpus Snapshot

- Average project description length: 35.7 words
- Average sentence count: 2.2 sentences
- Most common length: 2 sentences
- Distribution: 16 one-sentence entries, 36 two-sentence entries, 21 three-sentence entries
- 34 of 76 descriptions begin with `A`, `An`, or `The`
- 39 of 76 entries list collaborators in metadata rather than in the body
- 9 of 76 descriptions use inline HTML links, but most are plain text

## Core Voice

Project descriptions on the page are short, concrete, and concept-first. They usually do two jobs at once:

1. Name the format, system, or interaction in plain language.
2. Explain the social, perceptual, or conceptual twist that makes the work matter.

The voice is:

- Direct, not promotional
- Curious, not declarative
- Technically literate without showing off
- Specific about materials, interfaces, or behaviors
- Willing to pivot from mechanism to implication in a single sentence

The bio block is longer and more cumulative, but it reinforces the same tone: active verbs, concrete media, light humor, and an interest in misuse, society, and alternative futures.

## Default Structure

Use this as the default template:

1. Sentence 1: identify the work by medium and mechanism.
2. Sentence 2: name the payoff, tension, or frame.
3. Optional sentence 3: add context such as venue, commission, residency, scale, or support.

Example shape:

`A/An [format or object] that [does something specific]. [Why that matters, or what it asks the viewer/user to notice]. [Optional context].`

## Sentence Patterns

Common openings:

- `A ...`
- `An ...`
- `Ongoing ...`
- `Real-time ...`
- `Thousands of ...`

Preferred sentence behaviors:

- Start with the thing itself, not with abstract framing
- Use active constructions over passive when possible
- Let one sentence carry the mechanics and the next carry the implication
- Use a question only when the project is explicitly framed as a provocation

## Diction

Favor:

- Concrete nouns: `installation`, `app`, `tool`, `performance`, `map`, `browser extension`, `dance performance`
- Specific verbs: `tracks`, `matches`, `visualizes`, `intercepts`, `scrambles`, `projects`, `organizes`
- Technical terms only when they are part of the work's actual method
- Slightly strange or playful phrasing when it sharpens the idea

Use with restraint:

- Big abstract nouns without grounding
- Adjectives that only signal quality, scale, or novelty
- Internal process language
- Long lists of technologies

## Point of View

Default to third-person description.

Use first person only when the work itself is autobiographical, performative, or inseparable from the artist's own action. The corpus includes a few first-person entries, but they are exceptions tied to the premise of the piece.

## Metadata vs Body

Keep these out of the description when possible because the card already has places for them:

- Year
- Collaborators
- Client
- Link inventory

Put those in metadata fields unless the collaboration or commission is central to understanding the work.

## What To Avoid

- Marketing copy
- Mission-statement vagueness
- Overexplaining process details
- Repeating the title in the first sentence
- Empty praise words like `innovative`, `cutting-edge`, `immersive` unless the next phrase makes them concrete
- More than three sentences unless the piece truly needs a longer setup

## Recommended Constraints For New Entries

- Target 25 to 55 words
- Prefer 2 sentences
- Make sentence 1 legible to a reader scanning quickly
- Make sentence 2 do the conceptual or social work
- Add a third sentence only for crucial context

## Working Template

Draft against this checklist:

- Can the first sentence stand alone as a plain description of the project?
- Does the second sentence add tension, stakes, affect, or context?
- Is every technical term doing real work?
- Would the text still make sense if read out of context in a grid?
- Is the description short enough that the image still carries equal weight?
