# The final check

Do this after the last round of changes, before a chapter counts as finished. It has two parts: the script, then a full read-through.

## Part 1: the script

```bash
python3 .claude/skills/chapter-rewrite/scripts/style_check.py "New - Re-plan/Volume N/Chapter N - Title.md"
```

Go through every section of the output. A count isn't a fault; it's a place to look.

- **Spelling, dashes, dots, quotes, double spaces:** these should all be zero. Fix any hits.
- **Bold, THOOM, italics, corner brackets and `---`:**
  - THOOM is only ever his heartbeat.
  - Italics are only for thought, stress and established sounds.
  - Every `---` is a real shift of time, place or viewpoint.
- **Oaths:** is the same oath used the same way twice?
- **"nothing":** is each one doing work?
- **Fingerprint phrases:** check every hit.
- **Gesture clusters:** where the same gesture falls within six lines, change one of them to something specific to that person and moment. Old Craft Rules §4 lists better options.
- **Repeated six-word runs:** decide whether each repeat is deliberate. For example, a character's verbal habit is fine; an accident isn't.
- **Paragraph rhythm:** the median should be around 14–22 words. Every paragraph of five words or fewer should be a real narrowing of attention.
- **Untagged dialogue runs:** make sure the speaker is never in doubt.

## Part 2: the read-through

Read the whole chapter, start to finish, with these questions.

**Decisions**

- List every decision in `Decisions.md` that touches this chapter, and find each one on the page.
- Nothing new is named or characterised without the author. Every new trait, person or world fact was flagged **Your call** and has an answer.

**The principles**

1. Is every character still themselves? Alaric keeps his kindness, wits and humour, even with no past.
2. Which small answers does the chapter give, and which big ones does it keep back? It should do both.
3. Does any passage explain how something works instead of living it?
4. Does the chapter test the volume's question without answering it?
5. Does any sentence tell the reader what a moment means? The two places to look:
   - the last sentence of each paragraph;
   - narration that says what a character then says aloud.
   - every comparison ("like", "as if", "as though", "the way"): could the viewpoint character make it from what's happened to them on the page? And every fancy word: would a plain one do?
6. Does every major character in the chapter want something, and does the chapter threaten it?
7. Does each borrowed trait stay a trait, without importing the borrowed character's story?
8. Does every inner spiral say something new on each turn?

**Continuity and staging**

- Time of day and light, and what that means for what can be seen.
- Where every object is: who holds it, and where it was put down.
- Bodies and props: moved when touched, and still there when not.
- Clothing, blood and injuries.
- What each character knows, and when they learned it.
- What the viewpoint character worked out in earlier chapters. He shouldn't ask a question he has already answered himself. For example, in Chapter 2's draft the boy asked why the elves came, after deducing it in Chapter 1.
- Where the light comes from in every scene: torch, fire, moon, candle. When a light leaves, what can still be seen?
- Which hand is doing what, especially after a hand has been hurt, burned or taken away.
- Numbers: ages, years and distances.
- What the viewpoint character can physically see and hear from where they are.

**Point of view and speakers**

- Every fact and inference belongs to the viewpoint character.
- Every untagged line is clear from context.
- Every pronoun that follows a sentence about someone else still points to the right person.

**Repetition**

- Strong verbs repeated across the chapter (Chapter 2's draft had "caught" nine times, "tore" nine and "dragged" six). The style check lists the most repeated words.
- Description repeated from an earlier chapter. Once the reader knows the layered voice, "the layered voice" is enough.

Check each of these for the same thing happening twice:

- a question;
- an intervention (such as "leave that alone");
- a gesture;
- a laugh;
- an oath;
- a phrase.

**Character**

- Alaric's guardrails: no sixth sense for danger, no hidden mastery, no polished explanations of himself.
- A wrong belief is reached by reasoning, and isn't corrected on the page.
- Each person shows fear in their own way (design bible §9.4). For example, Gerolt gives instructions, and Alaric looks for a rule.
- Voices pass the swap test (design bible §7.6): an important line couldn't be moved to another character without sounding wrong.

**Structure**

- By the end, something has changed that can't go back.
- The viewpoint character makes a real choice.
- The ending is a hook.
- The title works twice.

**Knock-on effects**

- Did any change alter the meaning of a line elsewhere, in this chapter or the next?

For anything this list doesn't cover, see `Old - Before Re-plan/World Bible/Chapter Craft Writing Rules.md` §24, the long form.

## After the check

- Fix objective faults as a new round in the change list, and re-run `apply_changes.py`.
- Put judgement calls to the author as numbered questions, each with a recommendation.
- Commit and push.
