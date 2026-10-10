---
name: chapter-rewrite
description: The method for rewriting, revising or reviewing a chapter of the web novel "The Ruler of Nothing" with its author, learned on Chapter 1. Covers where canon lives, how to work with the author, the agreed writing principles, the house style, before/after change lists and the final check. Use it whenever the author wants to rewrite, redraft, revise, tighten, critique or plan any chapter or interlude (Chapter 2 onward, or Chapter 1 again), shares a draft, asks what's wrong with a chapter, or wants to see changes as a before and after, even if they don't mention the skill.
---

# Rewriting a chapter of The Ruler of Nothing

The author is re-planning a fantasy web novel of at least twelve volumes, one step at a time. The re-plan began because "characters don't feel like characters". Chapter 1 was revised with the author over several rounds. This skill records what worked, so every later chapter gets the same care without relearning it.

Read `references/chapter-1-lessons.md` once before your first chapter. It shows each lesson as a real before and after, with the author's verdict.

## Where the truth lives

Read these before touching a chapter. When two sources disagree, the higher one wins.

1. **`Story Bible/Decisions.md`.** Every decision made with the author, the questions still open, and the old files that now conflict. It overrides everything below it. Read the sections for the volume, the chapter, and every character and place in it.
2. **`Story Bible/Handoffs/Claude Handoff (1 October).md`**, the newest consolidated handoff (start with its §22–24), and the earlier **`Story Bible/Handoffs/Claude Handoff (29 September).md`** (added 29 September), kept as a historical source. The author also works in a second workspace; its chapter copies can lag behind this repo's, so check that a handoff's quotations match the chapters here. The author's work outside this repository on 28–29 September: the line pass of Chapters 1–3, Chapter 4, the philosophy, the Eight Rulers, the shared soul, the approved survival ending, love, and a proposed Volume 1 structure. What the author set there is copied into `Decisions.md`; everything else in it keeps its own label (**author-set**, **working consensus**, **unapproved proposal**, **strong recommendation**, **still open**). Never treat a recommendation in it as decided.
3. **`Story Bible/Volume N Picture.md`.** The shape of the volume: its question, arcs and ending.
4. **`Manuscript/Volume 1/Chapter 01 - A War Without Sound.md`.** The model chapter for voice, rhythm and page style. For Seralune's voice, `Chapter 04 - A Promise Left Fractured.md`.
5. **`Story Bible/Craft/Narrative and Web-Novel Design Bible.md`.** The craft reference. The most-used parts:
   - §2.3, the house page style;
   - §7.5, character voices;
   - §9.4, how each character shows emotion;
   - §9.6, italics;
   - §17–18, scene and chapter design;
   - §19.3, horror through absence.
6. **`Archive/World Bible/`.** The lore record, but only where `Decisions.md` doesn't override it. `Chapter Craft Writing Rules.md` §24 is the long final checklist.

**Check every branch, not only main.** On 29 September, five rounds of Chapter 4 and 5 design, with decisions the author had made, were found on `claude/youthful-curie-i1c390`, never merged. Before starting, run `git fetch origin` and `git log --oneline main..origin/<branch>` for each branch, and bring in anything unmerged.

The old chapters in `Archive/` are raw material, not canon. Many of them conflict with decisions; the list is under "Existing files that now conflict" in `Decisions.md`.

## Where files go

The repository was reorganised on 6 October 2026. Keep to this layout, and use two-digit chapter numbers in file and folder names so they sort in order ("Chapter 04", "Chapter 10"). The heading inside a chapter stays "# Chapter 4 – Title".

- **`Manuscript/Volume N/Chapter NN - Title.md`**: finished chapters only, the ones the author has accepted.
- **`Chapter Development/Volume N/Chapter NN/`**: everything else about one chapter. That means its design (`Chapter NN - Design.md`), dialogue rounds, revision notes, comparisons with the old chapters, and changes files. A chapter being drafted lives here as `Chapter NN - Title.md` until the author accepts it. Then it moves to `Manuscript/` with `git mv`, and its live change list's `"chapter"` path is updated.
- **`Chapter Development/Volume N/Chapter NN/Drafts/`**: that chapter's saved drafts and its change lists. A saved draft is never edited.
- **`Chapter Development/Volume N/`** (top level): working documents that cover several chapters, such as a review of several chapters at once.
- **`Story Bible/`**: canon and planning. That's `Decisions.md`, the Volume Pictures and the Volume 1 outline. The author's handoffs and Claude's replies to them go in `Handoffs/`, proposals that aren't canon in `Proposals/`, and the craft reference in `Craft/`.
- **`Archive/`**: everything from before the re-plan, unchanged.
- **Word-for-word files stay word for word.** The author's handoffs, proposals and pasted designs or dialogue keep their original text, even where it names a file by an older path.

## How to work with the author

The rules below come from the author's own instructions ("Never accept my words as FACT, challenge me, ask questions, understand what I want, never name character or give them characterizations without my input, lets do this all together 1 step at a time").

- **Challenge, including the author.** Check what they say against the decisions and the page. If something doesn't hold, say so plainly and explain why. They want a collaborator, not a typist.
- **One step at a time.** Ask a few questions at once, each with your recommendation and the reason for it, then wait. They answer by number and often briefly ("1. yes 2. keep"), so number everything.
- **Ambiguous answers get a follow-up.** For example, "Yes" to an either/or, or "them in particular". Ask again with concrete options instead of guessing, because a wrong guess ends up in the manuscript.
- **Never invent character without asking.** Don't name a character, or give one a trait, habit, backstory or relationship, without the author's input. When a draft genuinely needs something new (a behaviour, a neighbour, a piece of lore), write it in and mark it **Your call** so they can say yes or no.
- **Recommend; don't list everything.** Give your pick and why. Mention an alternative only when it's a real contender.
- **Say what's yours.** Mark new lines, images and world facts as new. The author rejects what doesn't sound like them, and that's how the voice stays theirs.
- **Keep the record current.** Put each answer into `Decisions.md` as it's given, and move answered questions out of "Open questions". Commit and push after each round, following the session's git instructions.
- **Plain words.** Explain craft terms the first time. Keep chat short and put the detail in files.
- **The old chapters' characters are out of date.** They were written before the characters were redesigned. Re-voice every character from `Decisions.md`, never from the old draft. For example, Gerolt must sound like Cid. The author: "this is the same for all future chapters we rewrite".
- **Design important dialogue together.** The author: "I will give my input on how important lines between characters must read, with your input as well. I often tend to put it in my own voice, but you move it from my voice to the characters we agreed." Before drafting, list the chapter's key exchanges and ask for the author's rough version of each. Give it back in the character's agreed voice, show both side by side, and keep what the author meant. Their words are the intent; the voice comes from `Decisions.md`. **Plain beats clever.** Offered a plain line ("Suppose that's goodbye, then") and a joke built on a Chapter 1 detail ("Never did get those shutters to sit right"), the author chose the plain one: "A is better, more human-like. B sounds robotic." A line that's clever about the story, rather than about the person in front of them, sounds written. **The same goes for thoughts, and for anger** (Chapter 4). "That tree hasn't grown a hand's width in my whole life" was "explaining things… doesn't make any sense"; the author's version is what a shocked person thinks: "How in the world did the tree grow so big? Yesterday it was way smaller." And a character who breaks should break. "Were you told to stand there and call me 'Your Highness' until I stop asking?" "doesn't sound angry at all. Seralune must break here, like 'ARRGHH, WHY CAN'T ANYONE JUST SAY WHAT IS GOING ON!?'" A cutting question is control; a scream is losing it. **Don't chop speech into short parallel sentences.** "He killed one. He cut the other one apart." was "robotic", and so was "Something set them off. Scouts don't come at a farmhouse like that. What happened back there?" ("make it one sentence"). People run their thoughts together when they talk: "He killed one and cut the other one apart." **The same goes for description.** "A bridge crossed the river there. At its near end stood a hut… A rider sat his horse among them. The lantern caught his pale hair…" drew "make the sentences combine so they don't sound robotic". A run of short, same-shaped sentences reads like a list. Join what belongs together, and keep short sentences for real jolts. **But not "and…and" everywhere** (Chapter 6 review): the run of "and" suits a capture or a fight, where things arrive faster than he can take them in. In calmer description (a creature's look, a town, a ship passing) it flattens the emphasis, so give selected details their own sentences.
- **What makes a voice** (handoff §2, 28 September). Characters answer one another; they aren't "lore terminals exchanging declarations". Emotion changes the words: "I don't know" with no frustration, shame, disbelief or reason is usually too empty. A verbal tic ("Lad", "Look here") isn't a voice; voice comes from motive, relationship, rhythm, evasion, humour, vocabulary and what the character will admit. Every line is after something: an answer, reassurance, concealment, control, connection, resistance or a decision. Speakers are always clear, and "said" and "asked" are welcome.
- **Restraint isn't voice** (Chapter 10, rejected three times: 2 October, 4 October and 5 October). The rejected rounds piled up rules like "no articulate speeches", "keep it short" and "her silence is the danger". The result was soft, interchangeable lines and report prose ("Nereth said nothing." "Seralune waited."), and the author felt "no emotion… no horror… just words and then a weird explosion". A descent into madness needs the character present and wrong, one new kind of wrong at a time, with a cause the reader can watch. A climax needs to be built up on the page beforehand. When a chapter has agreed voice references (Seralune as Alisaie, Nereth as Ram), check every line against them before sending.
- **Stop when revising would only make it different** (handoff §2–3). Chapters 1–4 "are good and no longer need broad rewrites". Further gains come from causality, continuity, voice or exact prose, "not from making every line louder". Don't run general beautification passes.
- **Never write a chapter without warning.** The author: "Before you write any chapter, let me know in advance so I can read the chapter design first, and we can plan some dialogue options before then write the chapter." The order is always: the design, agreed; a round of dialogue options for the key exchanges; then say the chapter is ready to write, and wait for the go-ahead.
- **One chapter at a time.** "I prefer designing chapter by chapter." A plan across several chapters stays a rough outline; the detail goes in the current chapter's own design file (`Chapter Development/Volume N/Chapter NN/Chapter NN - Design.md`).
- **Plan enough to happen** (29 September). The author: "The chapters we are creating are far too short for my liking… little in content, where I prefer more." Chapters 3–5 came in at 2,000–2,600 words, against Chapter 2's 4,660. Don't design a chapter down to its fewest beats. Give the people in it room to push on each other and react, and give the viewpoint character a choice the reader can see. The extra never comes from lore, decoration or explaining (principle 5 still holds). The target (29 September) is 4,000–5,000 words, and longer whenever "storytelling and character writing can be done better". **Length comes from what happens, not from word budgets.** Chapter 5's deep revision budgeted about 4,300 words scene by scene, but everything agreed, written at the density the author likes, came to under 2,900. Padding to a number breaks principle 5. So plan the events, and check the design against the target before the dialogue round: enough exchanges, reactions and choices to fill it. **It happened again on Chapter 6:** budgeted at 6,500, the agreed chapter came to about 5,100. Per-scene budgets run about a quarter high, so give the author a range before drafting, not a single number, and say it's an estimate.
- **Ask "What could make this chapter 100/100?"** (30 September, the author's requirement for this and every future chapter proposal). Answer it in the design file with specific improvements and honest challenges: what still limits the design, the strongest openings, the risks, and what to test in the draft. Don't treat a working outline as the best version, and don't answer with bigger spectacle, more suffering or more words.
- **Search the whole chapter before claiming what someone said or knows** (30 September). Claude said Alaric named Gerolt first in Chapter 3; the author pointed out Silas shouts "Gerolt died for nothing!" earlier, and Alaric notices ("He knew Gerolt's name."). Grep the chapter for the name or line before building an argument on it. **It happened again on Chapter 7:** the design called Cyrandor a stranger, but Chapter 5 already had him bow and smile in the corridor. Before designing a chapter, search the chapters before it for every character in it.
- **Don't fix a plot problem by taking something away from a character** (30 September, Chapter 6). To make Alaric's walking off after a forest warning believable, Claude had Silas refuse to explain what an ogre was, and leaned on Alaric's amnesia. The author refused on both counts: "amnesia should not erase the obvious danger", since he keeps general understanding, and the non-answer broke Silas's rule of answering practical questions and evading personal ones. "We should allow an intelligent character to make a bad decision. We do not need to remove his understanding to make the decision defensible." Fix it with motive instead: he understands the danger and underestimates it, because staying feels worse.
- **Seralune's thoughts are Alisaie's** (29 September). Offered two plain thoughts for her, a memory of Elowen and her decision to keep a secret, the author sent both back: "make it like something Alisaie would think". Give every thought of hers that shape before offering it. She's sure of what she knows, reasons from it out loud in her head ("So she's new, or she's lying to me, or…"), and turns to the next practical step. The Chapter 4 model, in the author's revision of 1 October: *Very well. If I'm alive, I can get up. Then I'll find out where I am.*
- **A thought reasons; it doesn't just ask** (29 September, the author's review of Chapter 5). About thirty italic thoughts, most of them question lists ("Why are so many people here?", "Why is he so on edge?"), repeated what the prose had already shown. Chapter 4 worked because her thoughts deduced. At the door with no inside handle, in the author's revision of 1 October: *No handle on this side. Whoever shut that door didn't mean for me to open it.* Keep thoughts that reach a conclusion or break on one; cut those that restate the scene, and never note the same thing twice. At the chapter's biggest realisation, let her add the evidence up and flinch (*So it's been…* / She didn't let herself finish it.).
- **A one-line fix is still prose** (29 September). The author called Claude's fix "He had the sword and wanted to help. He tried to go down to Gerolt, but his knees would not unlock." robotic: two short "He…" sentences side by side read like a list, and "his knees would not unlock" reads like a report. Give every fix the robotic test before showing it, and prefer one sentence that runs the way his thought runs.
- **Challenge the author's own lines, and build a better one.** The author: "I want you to always challenge me and ask questions, which is good", and "if you have a better constructed sentence, tell me." Check their line against the page: where the character is, what they've just done, what they can know. On Chapter 2 the author offered "He tried to continue moving, ever closer towards Gerolt, but his legs just won't move": he had already stopped, so there's nothing to continue, and "ever closer" says he gets nearer when the point is that he can't. Say so, then offer a version that keeps what they meant, using their own words where they work ("just wouldn't move").
- **When a line changes, re-read its neighbours.** The line pass changed Silas's question to "How did you know him?" and left the old answer, "He didn't."; it had Alaric "try to stand" three paragraphs after he stopped on his feet; and Silas told a standing Alaric to "Get up". A changed question can strand its answer, and a changed action can contradict where someone is.
- **The world keeps moving** (10 October, the Chapter 11 working design): "The author explicitly wants an inhabited world." Markets, auctions, deliveries, household work and customers' talk run on their own schedule, and the viewpoint character leaving doesn't stop them; any interruption needs a cause inside the world. Don't make every worker, customer or encounter an instrument of his arc: people have their own business, and what he reads into them is his and can be wrong. Because he only sees what happens while he's there, the continuing world shows at the edges (the next lot already waiting, a voice still calling behind him).
- **Stay in one pair of eyes.** "Always stay in Alaric's eyes when the chapter is about him." Don't cut away to show what he can't see; let him see it from where he is. On Chapter 2, that means Gerolt's last stand is seen from where Alaric is. **The narration follows his attention.** He's staring at Gerolt, so "The man crossed to him in a few strides" became "The man was at his side before Alaric had noticed him move" (the author: "The man was at him before he noticed, something like this"). **Show a beat the way he sees it, step by step, not as a summary line.** On "Wena looked from Gerolt to them. Then she came after them.", the author said: "Scenes like this are like just saying it for the sake of it. Remember it's all in Alaric's perspective: he saw Wena staring at Gerolt, then at them, she paused for a brief moment, then ran after Alaric."

## The principles

These are copied from `Decisions.md`. If the two ever differ, `Decisions.md` wins, and this list should be updated.

All eight are agreed.

1. **Amnesia removes history, not personality.** Alaric is "still himself, without knowing who he is". He is kind, smart and caring, and his humour survives: "a headache that's at least probably my own".
2. **Small answers constantly; big ones withheld.** Chapter 1 gives the reader Mydea, Gerolt's name, 『Affinity』, the Faint, Natharul and "Empty". It withholds who he is, the running figure and the silent battle.
3. **Live the rules; don't explain them.** Never set out how something works "on paper like a thesis". Characters think the way amnesiac Subaru does in Re:Zero Arc 6 (Chapter 57 onward). For example, the line "He didn't know what his own voice sounded like." stays. The line "He understood the word completely. He couldn't remember the life it was meant to describe." was cut.
4. **A volume tests its question; it doesn't hand over the answer.**
5. **Don't explain the meaning.** In the author's words: "I don't like over explaining meaning that make readers think beyond the obvious." Show the plain thing and stop. Cut any sentence that tells the reader what a moment means, and any image that hints so hard it pushes readers past what's on the page. This is the rule the author enforced most on Chapter 1: they rejected one added image and cut fifteen explaining lines, seven of them their own.

   **The same rule covers words chosen to sound good.** The author, on Chapter 2: "explaining things for the sake of it, using words to make it look cool… this is from Alaric's POV, how would he know this." Their example was "a sound like an axe going into green wood": he has never heard an axe go into wood. So:
   - A comparison ("like", "as if", "as though", "the way…") is allowed only when it points at something the viewpoint character has lived through on the page. For Alaric in Volume 1, that's almost nothing. "Gerolt's flame had sat in his palm no bigger than a candle's" passes; "like water down a drain" doesn't.
   - Don't dress up a plain thing. Use "leave splinters in his hair", not "comb splinters through his hair". Use "burst", not a third "punched".
   - Before showing a draft, search it for comparisons (the style check lists them) and defend each one or cut it. Chapter 2's first draft lost thirteen lines to this.

   **Don't tell the reader what they already know** (27 September, on the redesigned Chapter 2). The author: "You don't need to explain things like this, because the reader will know he stopped laughing. Laughing doesn't last forever." And: "'He stayed on his knees.' The reader knows he is on his knees." A line that only reports a laugh ending, a pause, or someone staying where they were "draws the scene away". Cut it, unless the pause itself is the event. The style check lists short lines of this kind.

   **But add meaning where he'd feel it** (27 September). The author: "I see a lot of someone did X, he did Y. Just add meaning to things." For "Alaric didn't get up. He couldn't look away from Gerolt.", they wanted: "Alaric couldn't get up. He was staring at Gerolt. That old man had taken care of him until his dying breath, and now Alaric was going to leave him there and never see him again." Where the two rules meet:
   - The narrator never interprets, decorates or hints.
   - Alaric feels and understands things in plain words, in the moment, about what's in front of him.
   - At a moment that matters to him, a run of bare actions is a fault. Fights can stay fast.
   - **Keep the meaning small and concrete, and only where it's needed.** "It was the only place in the world he knew" was "too melodramatic". The toned-down "He had woken under it that night, with a blanket over him and stew on the fire" was still "too much", so the house burns without comment. The moments the author wanted meaning at were the ones about Gerolt: the sword, his feet stopping, the fire going out, being dragged away.
   - **Make "it" clear.** The author read "Alaric waited for it to come back" and asked "what is it?" Name the thing, and let the line say what it meant to him: "Alaric waited for the fire to come back. It had kept burning through both arrows, and now it was out…"

   **It never silences the viewpoint character** (agreed 27 September). The rule stops the *narrator* explaining; it doesn't stop Alaric thinking. Chapter 2 was cut so hard that he had no thoughts on the page while Gerolt died for him. Give him his thoughts at the big moments, in his own words and in the moment: *Get up. Why won't you get up.* is Alaric; "the word *I* had somewhere to stand" is the narrator explaining. When he's frightened he has Subaru's mouth, running inside his head (see `Decisions.md`, Alaric).

6. **Every major character wants something the story threatens.** Know each character's want before writing a scene, and let the chapter press on it. Gerolt wants his peace with Wena; a stranger in his only bed and "men at my door" by noon end it. The boy wants to know who he is; the riders might know him, and he chooses silence.
7. **Borrowed characters lend specific traits, not templates.** Take the named trait and nothing else, and record in `Decisions.md` which trait came from where. Gerolt takes Cid's humour over damage, not Cid's life or story. The rest of the cast's borrowed traits are listed under each character in `Decisions.md`.
8. **An inner spiral must change what it claims each time it turns.** When a character circles a thought, each turn must say something new: a new fear, a new conclusion, or a new cost. Repeating "why me" in bigger words isn't movement (design bible §9.1). This matters most for set pieces like the tear, where "Why did this happen? Why did I do it? Why me, when I'm empty?" are three different claims.

New principles from the author go into `Decisions.md` first, then here.

## The method

### 1. Read

Read the whole chapter, the decisions that touch it, the volume picture, and the chapters on either side.

Find out which lines the author wrote personally. For example, diff the chapter against its old versions in `Archive/`. On Chapter 1, the author had written the opening; the rest was an older rewrite. The author's own lines get the lightest touch, and every change to them is flagged.

### 2. Write the revision notes

Create `Chapter Development/Volume N/Chapter NN/Chapter NN - Revision Notes.md`, with line numbers throughout, in these sections:

1. How the chapter works (what to keep, and why it works).
2. What already matches the decisions.
3. Changes the decisions require, grouped by character.
4. Craft fixes.
5. What's undecided and needed before revising.
6. Old callbacks that no longer bind this chapter.

This shows the author you understood the chapter before changing it. It also keeps "this is good" apart from "this must change".

### 3. Ask the undecided questions

Ask them a few at a time, each with a recommendation. Record every answer in `Decisions.md` before writing.

### 4. Save the draft

Copy the chapter, unchanged, to `Chapter Development/Volume N/Chapter NN/Drafts/Chapter NN - Title (Draft K, before revision).md`. Every change you make is measured against this copy, and anything rejected goes back from it.

### 5. Write the change list, then apply it

Don't edit the chapter by hand. Write each change as an entry in `Chapter Development/Volume N/Chapter NN/Drafts/Chapter NN - change list.json` (format below), then run:

```bash
python3 .claude/skills/chapter-rewrite/scripts/apply_changes.py "Chapter Development/Volume N/Chapter NN/Drafts/Chapter NN - change list.json"
```

It applies the list to the saved draft and writes both the revised chapter and `Chapter NN - Changes.md`, in the chapter's development folder. The changes file shows every change's before, after and reason. Doing it this way means the changes file can never drift from the chapter. The author approves or rejects change by change, and a rejection is a one-word edit followed by a re-run.

When writing changes:

- **Change only what's needed.** That means what the decisions, the principles and real craft faults require. Say what you left alone on purpose, and why.
- **Match the chapter's voice.** New lines should read as if the author wrote them.
- **Prefer cutting to adding.** When you must add, use the smallest concrete action or line that does the job, and test it against principle 5 before showing it.
- **Watch for knock-on effects.** On Chapter 1, Gerolt naming Natharul at the window changed the meaning of the name he swallows when the riders arrive. Flag effects like that.
- **Keep the numbering stable.** Once the author has referred to a change by number, never renumber it. Add later rounds at the end of the list. To adjust an earlier change, edit that change and note it in its reason; the script refuses a change stacked on top of another.

**If most of the chapter will change**, for example when writing Chapter 2 from the old material, paragraph-level change lists become unreadable. Instead:

1. Agree the chapter's plan with the author first: what changes by the end, which decisions it carries, which small answers it gives and which big ones it withholds, and the choice its viewpoint character makes.
2. Write the new chapter.
3. Save the old version in the chapter's `Drafts/` folder.
4. Present the changes scene by scene, with the key passages as before and after.
5. From then on, use change lists for every later round.

### 6. Present

Send the changes file. In chat, quote the few most important additions briefly, then list every **Your call** item as a numbered question.

### 7. Record the answers

On each answered change, set `"decision"` to `"accepted"` or `"rejected"` and add a `"decision_note"`. Re-run the script, update `Decisions.md`, then commit and push.

A new general preference from the author, like principle 5 was, goes into `Decisions.md` and into this skill. Then apply it to the rest of the chapter, including the author's own lines, but only after asking.

### 8. Final check

Run the mechanical check:

```bash
python3 .claude/skills/chapter-rewrite/scripts/style_check.py "Manuscript/Volume N/Chapter NN - Title.md"
```

Then read the whole chapter through, using `references/final-check.md`. Fix objective faults (spelling, pronouns, continuity) as a new round in the change list. Anything that needs the author's judgement goes to them as a question.

## The change list format

```json
{
  "title": "Chapter 2: Changes",
  "draft": "Chapter 02 - Title (Draft 1, before revision).md",
  "chapter": "../../../../Manuscript/Volume 1/Chapter 02 - Title.md",
  "changes_file": "../Chapter 02 - Changes.md",
  "intro_md": "Markdown under the title: the date, the rounds, where the draft is saved.",
  "glance": ["Extra lines for 'At a glance', such as a repeated beat counted before and after."],
  "summary_md": "## What each decision became\n\n1. **The sword:** change {tag:sword}.",
  "sections": {"The cabin": "The cabin (draft lines 243–581)"},
  "changes": [
    {
      "section": "The cabin",
      "title": "A short name",
      "kind": "changed",
      "tags": ["sword"],
      "before": "The exact paragraph(s) from the draft. Separate paragraphs with a blank line.",
      "after": "The new paragraph(s).",
      "why": "Which decision, principle or craft fault this serves.",
      "call": "Optional: what's new here and needs the author's yes or no.",
      "decision": "accepted",
      "decision_note": "What the author decided, shown on the change."
    }
  ]
}
```

- **Paths** are relative to the change list's own folder, the chapter's `Drafts/`. From there a saved draft is just its name, the changes file is `../Chapter NN - Changes.md`, and a finished chapter is `../../../../Manuscript/Volume N/Chapter NN - Title.md`.
- **`kind`** is one of:
  - `changed`: `before` becomes `after`.
  - `cut`: leave out `after`.
  - `added`: `before` is the paragraph the new text follows, and it stays; `after` is only the new text.
- **`before`** must match the draft exactly and appear only once. Include a neighbouring paragraph if it doesn't.
- **`{tag:x}`** anywhere in `intro_md`, `glance` or `summary_md` becomes the numbers of the changes tagged `x`.
- **Optional fields:**
  - `decision_short` gives the decided list a shorter note.
  - `--check` reports whether the files on disk are current, without writing anything.
- **Worked example:** `Chapter Development/Volume 1/Chapter 01/Drafts/Chapter 01 - change list.json`. It holds 62 changes over eight revisions.
- **Chained lists.** When a chapter changes outside this process (as with the line pass of 28–29 September), save the chapter as it stood as a new draft, point the old list's `"chapter"` at that draft, and start a new list from it. The old list and its changes file stay true, and `--check` passes on both. **For Chapters 1–6, the live list is now `Chapter NN - change list (author's revision).json`** in each chapter's `Drafts/` (the author's Word file of 1 October); later rounds go there. The lists before it (Chapters 1–3's line pass, Chapter 4's from "Before Evening", Chapter 5's deep revision, Chapter 6's first draft) end at the saved drafts. Chapter 7's live list is still `Chapter Development/Volume 1/Chapter 07/Drafts/Chapter 07 - change list.json`.

## House style

This is the short form. The full rules are in the design bible §2.3 and the old Craft Rules §4.

- **British spelling:** towards, colour, armour, grey, recognise.
- **Quotes and dashes:** straight quotes; em dash with no spaces; the single "…" character.
- **Paragraphs:**
  - One speaker per paragraph.
  - Re-anchor the speaker after an action, or after more than two untagged lines.
  - A pronoun after a sentence about someone else needs a name instead.
  - Connected prose for ordinary experience. A one-line paragraph only for a real narrowing of attention.
  - Median paragraph roughly 14–22 words. Chapter 1 sits at 14.
- **Italics:** only immediate unspoken thought (*Was I here with them?*), precise stress (*nothing*, *him*), and the knocks (*Tock.*), which are the chapter's precedent for sound.
- **Plain-text copies lose italics.** Twice on 29 September, a review the author passed on said the thoughts or the heading weren't formatted, when the file had them. It had been given a plain-text copy. Before "fixing" italics or headings, check the file, and tell the author the copy dropped them rather than changing anything.
- **No stress marks inside italic thoughts.** Un-italicising a word inside a thought to stress it (*What did I* do*?*) was taken out every time it came up in the accepted passes: Chapter 3's "do" and "was", Chapter 4's "doing". Stress in speech stays ("Just come *on*!", "*nothing*").
- **Bold:** only **THOOM**, which is Alaric's heartbeat and nothing else, plus very rare, purposeful sounds.
- **Typography:** keep 『Affinity』, 『Magic』 and 『Faint』 (the rank; the author, 1 October: "apply 『Faint』 to all chapter where it is used"). The ordinary word "faint" (a faint sound) stays plain. "Magic" is the ancient word, and Alaric thinks it but doesn't say it.
- **Section breaks:** `---` only for a real shift of time, place or viewpoint. The break after "forgot to breathe" in Chapter 1 is the author's deliberate exception.
- **Oaths are sparing and varied:** "By the Four", "Four preserve us", "By the Eight", "Before the Eight", "The Last Dark take you", "What in the Last Dark…". Don't repeat the same oath in the same way; Gerolt's "Easy, lad—by the Four" once is enough.
- **Those are Mydea's.** Natharul has its own (world bible, "Natharul oaths", two or three per Natharul chapter at most): "Root and crown", "Before the Tree", "May your roots find stone" and "Rootless", its worst insult. Never put the Last Dark in a Natharul mouth: Chapter 7's draft and Chapter 10's recommendations both did, and both were caught.
- **Watch-list:** "not X, but Y", "for a moment", "nothing answered", "almost heard", and the same eyes, hands, breath, jaw, shoulder or silence gesture close together. None of these is banned; check for clusters.
- **Comparisons:** only from what the viewpoint character has lived through on the page. Say plain things plainly (principle 5).
- **No horses' smell** (1 October): the author dislikes it. Use other concrete details.
- **No counting** (Chapter 4, then Chapter 10 on 5 October): "I don't like the counting, remove it." Don't have a character count breaths, steps or turnings, in thought or in speech.
- **Plain nouns:** "spattered the ground", not "spattered the leaves" (the author's note, 27 September).
- **Common words:** the author asked "what is bracken?", then "I don't like 'ferns'" either. If they don't know a word, many readers won't. When a detail is only there to say where something is, drop it rather than swap in another word for it ("He landed on his back"). Watch for British country words and trade words: bracken, eaves, pommel, sidle, and "sill", which the author called a buzz word (29 September: "remove 'sill'. [Stop] putting buzz words"). ("Bracer" was approved in Chapter 2.)
- **A nameless character's label** ("the man", before Silas gives his name) wears out fast. The author, on 22 in one chapter: "The man is said too much." Use "he" where only he can be meant, "a fist" or "a hand" where that's all the viewpoint character feels, another plain label now and then ("the stranger"), or cut it. Start a sentence from the person you mean, so "he" never has to be worked out.
- **"The dark":** the author, 27 September: "One thing I notice you do a lot is say 'the dark' a lot. Cut down on that, find other words." Say where something is, or what can and can't be seen ("somewhere below them", "Under the branches, the moon came through only in patches"). The style check counts it.
- **"Nothing"** is the series title word, so keep it rare and meaningful.
- **Point of view:** close third. Every fact and inference belongs to the viewpoint character, and he can only conclude what the page has given him evidence for. "*It's me. They're coming for me.*" drew "How does he know they are coming for him?" A frightened question ("*Why are they still coming?*") is fine; a conclusion he can't have isn't. The same goes for "already" about someone else: "Silas was already looking at the fire" drew "how does he know he is already looking at it?" He sees what's happening when he looks, not when it began. A man passing out can't know someone "talked through the whole walk back".
- **Alaric's guardrails** (old `Main Characters.md`): no sixth sense for danger, no hidden fighting mastery, no polished explanations of himself. His beliefs can be wrong, and he reasons his way into them.

## Files in this skill

- `references/chapter-1-lessons.md`: every lesson from Chapter 1 as a before and after, with the author's verdict.
- `references/final-check.md`: the read-through checklist for the final pass.
- `scripts/apply_changes.py`: applies a change list and writes the chapter and its changes file.
- `scripts/style_check.py`: counts what a script can count (spelling, typography, oaths, "nothing", "the dark", short lines that may tell the reader what they already know, comparisons, fingerprint phrases, gesture clusters, exact repeats, most repeated words, paragraph rhythm, untagged dialogue). It points at places to look, and doesn't fix anything.
