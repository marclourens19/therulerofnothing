# Re-plan: Decisions

Started 26 September 2026. This file records what the author has decided during the re-plan, in the author's own words where possible. Nothing goes under a "Decided" heading unless the author said it. Suggestions stay under **Open questions** until the author agrees.

Everything written before the re-plan now lives in `Old - Before Re-plan/`. That includes the World Bible, Main Characters and the chapter designs, and none of it has been updated. Where a decision contradicts those files, it is listed under **Existing files that now conflict**.

**The handoff (added 29 September).** On 28 and 29 September the author carried on the re-plan outside this repository. That work is summarised in `Claude Handoff.md`, which came with a line pass of Chapters 1–3 and the new Chapter 4. What the author set or accepted there is copied into this file, marked *(handoff §N)*. The handoff's recommendations stay in the handoff: its own labels (**author-set**, **working consensus**, **unapproved proposal**, **strong recommendation**, **still open**) say which is which, and none of its proposals is a decision until the author says so. Where the handoff changes something recorded here, the older line is marked *Superseded*. One file the handoff relies on, `Volume 1 Structural Map - Proposal.md`, is not in this repository.

## How we work

- One step at a time, together.
- Never accept the author's words as fact. Challenge them, and ask questions until the intent is clear.
- Never name a character or give one a trait without the author's input.
- **Whose eyes.** "Always stay in Alaric's eyes when the chapter is about him." *(Agreed 26 September.)* **The narration follows his attention** (27 September): "The man was at him before he noticed, something like this." **Show a beat the way he sees it,** step by step, not as a summary line (27 September). On "Wena looked from Gerolt to them. Then she came after them.", the author said: "Scenes like this are like just saying it for the sake of it. Remember it's all in Alaric's perspective: he saw Wena staring at Gerolt, then at them, she paused for a brief moment, then ran after Alaric."
- **"The dark"** (27 September). "One thing I notice you do a lot is say 'the dark' a lot. Cut down on that, find other words."
- **Rewritten chapters use the characters we decided, not the old drafts.** The old chapters were written before the characters were redesigned. For example, Gerolt must sound like Cid. "This is the same for all future chapters we rewrite." *(Agreed 26 September.)*
- **Important dialogue is designed together** (27 September). The author: "let's design conversations together in the chapter. I will give my input on how important lines between characters must read, with your input as well. I often tend to put it in my own voice, but you move it from my voice to the characters we agreed." So the author gives the line in their own words, and Claude gives it back in the agreed character's voice, with both shown side by side.
- **Stop when revising would only make it different** (handoff §2). Find what already works, find the exact sentence, transition, motive or continuity fault, make the smallest change that fixes it, re-read the whole scene, and stop. Chapters 1–4 "are good and no longer need broad rewrites": further gains come from causality, continuity, voice or exact prose, "not from making every line louder" (handoff §3). No more general beautification passes on Chapter 1.
- **Dialogue** (handoff §2):
  - Characters sound like people answering one another, "not like lore terminals exchanging declarations".
  - Emotion changes the words. "I don't know" with no frustration, shame, disbelief or reason is usually too empty.
  - A verbal tic ("Lad", "Look here", "Again. Slowly") isn't a voice. Voice comes from motive, relationship, rhythm, evasion, humour, vocabulary and what the character is willing to admit.
  - Every line is after something: an answer, reassurance, concealment, control, connection, resistance or a decision.
  - Short paragraphs and fragments are tools for real changes in perception, decision, danger or feeling, not the default rhythm.
- **Keep the statuses apart** (handoff §12). Decided, inherited-but-not-contradicted, later-volume concept and open are different things. Settle one mechanism at a time, and record whether the author approves it, rejects it or keeps it open.
- Principles settled here become the rules of the rewriting skill. The skill is `.claude/skills/chapter-rewrite/` (created 26 September, after Chapter 1). When a principle here changes, update the skill to match.

## Principles

### Agreed

1. **Amnesia removes history, not personality.** Alaric "is still himself, without knowing who he is."
2. **Small answers constantly; big ones withheld.** Volume 1 answers small questions often, so readers trust that the big ones will come.
3. **Live the rules; don't explain them.** Never set out how his memory works "on paper like a thesis". People don't think like that. He thinks and reacts the way amnesiac Subaru does in Re:Zero Arc 6 (Chapter 57 onward).
4. **A volume tests its question; it doesn't hand over the answer.**
5. **Don't explain the meaning.** In the author's words: "I don't like over explaining meaning that make readers think beyond the obvious." Show the plain thing and stop. Don't follow a moment with an image or a sentence that tells readers what it means or where to look. It covers both explaining a moment and hinting so hard that it pushes readers past what's on the page. *(Claude's reading, accepted with the cuts it led to.)* First applied in Chapter 1, revision 1: change 21 was rejected ("Nothing inside him answered either" stays), and changes 6, 19, 20, 25, 27 and 37 were trimmed. Revision 2 applied it to the author's own lines (changes 38–44). Lines 55, 143 and 645 were kept: they show or name something, and they don't explain it. **It also rules out comparisons the viewpoint character couldn't make, and words chosen to sound good** (added 26 September, on Chapter 2). The author: "One thing you're still doing which I said we should stop is explaining things for the sake of it, using words to make it look cool. This is from Alaric's POV, how would he know this." Their example was "a sound like an axe going into green wood". A comparison is allowed only when it points at something the viewpoint character has lived through on the page. For Alaric, that's almost nothing: Gerolt's flame, the stew, his voice. Applied to Chapter 2 (revision 1, thirteen lines) and Chapter 1 (revision 5, eight lines). The comparisons that remain are ones he can make: how the words land on him, the Light, Gerolt's voice and flame, his own hair, the layered voice, the knock's patience, and Gerolt's own "calling a dog". **Don't tell the reader what they already know** (27 September, on the redesigned Chapter 2). The author: "You don't need to explain things like this, because the reader will know he stopped laughing. Laughing doesn't last forever." And: "'He stayed on his knees.' The reader knows he is on his knees." **But add meaning where he'd feel it** (27 September). "I see a lot of someone did X, he did Y. Just add meaning to things." The author's example: "Alaric couldn't get up, he was staring at Gerolt, that old man had taken care of him until his dying breath and now, in this moment he was going to leave him and never see him again." *Claude's reading of where the two rules meet, to confirm:* the narrator never interprets, decorates or hints, but Alaric feels and understands things in plain words, in the moment. Keep it small and concrete: "It was the only place in the world he knew" was "kind of… too melodramatic" (27 September).
- **Common words** (27 September). The author asked "what is bracken?", then said "I don't like 'ferns'". Readers shouldn't meet a word the author doesn't know, and a detail that only says where something is can go. **It never silences Alaric** (agreed 27 September, with putting his thoughts back into Chapter 2: "We can do this together"). The rule stops the narrator explaining; it doesn't stop him thinking. Chapter 2 had been cut until he had no thoughts on the page while Gerolt died.
6. **Every major character wants something the story threatens.** *(Agreed 26 September.)* In Chapter 1, Gerolt wants his peace, and the boy ends it.
7. **Borrowed characters lend specific traits, not templates,** and we record which trait came from where. *(Agreed 26 September.)* For example, Gerolt takes Cid's humour and damage, not Cid's life.
8. **An internal spiral must change its claim on each turn.** Repeating "why me" with bigger words isn't movement (design bible §9.1). *(Agreed 26 September.)*

### Proposed, not yet agreed

- None right now.

## The series

- At least twelve volumes, possibly more: a story people come to love.
- **A long-form serial web novel** (handoff §2). A volume can run to forty chapters or more when its character movement, mystery and journey justify it; chapter count is never the target. The feel: the readability of a translated web novel with the lived-in depth of *The Hobbit* and *The Lord of the Rings*. Travel changes relationships, places hold history, quiet life gets room to matter, and consequences outlast the event.
- **Where the whole journey leads:** magic is removed by the end of the series.
- **The foundation (handoff §10).** The author supplied the quotation "God is dead. God remains dead. And we have killed him." The author's reading: people in this world have taken God's place and made themselves God. They claim the right to tell others who they are and what they must do, based on power assigned at birth. People are born equal and free, and the world would be better if they worked together. *The refinements in the handoff (§10, §16: equal worth rather than equal ability, "difference without domination", cooperation isn't automatically good) were recommended, not confirmed.*
- **The author's private north star (handoff §13):** "What are you, the reader, willing to sacrifice in service of this novel's meaning?" The in-story versions of the question in §13 are proposals.
- **The ending: approved direction** (handoff §17.1, 29 September). The author agreed with survival, and stressed that reaching it should take many volumes:
  - Alaric and Seralune **survive** the final unbinding.
  - They give up the shared cosmological exceptionalism that makes the world count them as one corrective soul. Alaric loses his extraordinary access to the Veiled powers; Seralune releases or loses the power that let her impose an answer on the world. Their compulsory magical dependence ends.
  - They go on as two separate, ordinary mortal people who can freely choose one another.
  - Magic ends through **collective participation**, not a private decision made by the two of them.
  - A child and family life later are wanted possibilities, not locked.
  - *Not settled:* the mechanism, the part Spirit and each Ruler play, the rules for a child, chapter titles, the number of volumes, any afterlife coda and the final image.
- **"A Promise Fulfilled"** (handoff §15.6). The author is drawn to this as the title of a chapter near the very end of the final volume, answering Chapter 4's "A Promise Left Fractured". Which chapter carries it is open.
- **Order of work:**
  1. Refine the new Chapter 1 until it's ready.
  2. Before writing Chapter 2 onward, discuss a picture of Volume 1, Volume 2 and Volume 3.

### Series timeline (approved 26 September; details to be built when we get there)

1. **Volume 1.** Chasing the past; the tear.
2. **Volume 2.** Darcy's rescue; the war comes home; Seralune and Nereth escape. Alaric and Freya become mutual. Both groups head for Kozmagar.
3. **Volume 3, Kozmagar.** The Time bearer searches for Alaric. Alaric and Freya become something serious. Seralune and Nereth arrive on the same continent; the two threads converge. **Alaric and Seralune meet at the end of Volume 3.**
4. **Volume 4.** Hostility, forced together. Freya's relationship is tested with Seralune present. Freya's choice comes near the end, or early in Volume 5.
5. **Volume 5.** A mission together; the pressure builds.
6. **Volume 6.** The slow fall into love.

These are rough shapes, not deadlines. The design bible warns against scheduling when people fall in love.

**Guard:** before they meet, their stories must keep affecting each other through cause and effect, never through near-misses.

### Approved direction (Claude's recommendations, 26 September)

- **Hostility comes from the tear, not a murder.** The world, and Redd most of all, hate her as the witch who killed thousands. She publicly accepts the blame; he privately believes it was him and stays silent. Their flaws collide: she decides for people, he refuses help.
- **Closeness is what's dangerous.** Hostility doesn't make them safe; it only means they aren't reaching for each other. *Superseded in part (handoff §17):* the series ending no longer rests on the Soul World ("finally able to love without endangering anyone"). They survive, lose what bound them, and choose each other as ordinary people. A Soul World reunion could still come after full mortal lives and natural deaths; whether it's shown is open.
- **"Time is broken."** The displacement left a thousand-year seam in time. Time remembers, and the tear reopened the seam. The Time bearer feels it as a wrongness, which is why "He's back" slips out.
- **Gilmot dies in Volume 2, for a new reason.** His threat no longer comes true, so his death becomes the group's moral test under the Volume 2 question: Silas wants any means, Alaric weighs it, and Darcy's choice is central. No one frees her by overruling her.
- **The border across a sea.** A narrow sea lies between Mydea and Kozmagar, and Mydea's coast is the frontier: forts, harbours and islands. Darcy's strategy held that sea; once she's stolen, beastfolk land on Mydean shores.
- **Why both groups end up in Kozmagar.** It's the one place neither Mydea nor Natharul controls. Both run there for the same reason and converge through Volume 3. The image of the meeting is still the author's to find.

### The author's earlier volume outline (working ideas, not locked)

1. Alaric and Seralune discover something is missing, but still choose to be themselves.
2. Freeing Darcy, killing Gilmot and going to the beast continent. Seralune and the Holy bearer are at odds with Natharul, and Thaeroval negotiates for his sister: politics. Maybe she and Nereth get away.
3. The Time bearer is on the move for Alaric. He wants to find him, or feels he needs to. Time is broken, but his predecessor was a great friend of Alaric's, and he wants to understand why. Seralune and Nereth reach the beast continent.
4. Seralune and Alaric meet, maybe. They don't like each other at all. Maybe Seralune kills Wena or Redd, but they join parties. This stops the love and her mana going haywire.
5. They have a mission together. Pressure builds among them.
6. They start falling in love, slowly.
7. Not thought beyond here yet.

## Volume 1

- **Goal.** Volume 1 isn't about answers yet. It's about:
  - world building;
  - understanding that something terrible happened a thousand years ago;
  - people suffering and places destroyed;
  - people who are racist, "magicist" and cruel;
  - danger, and the feeling of "I need to know more; maybe, just maybe, the next chapter will answer it."
- **Emotional question (the author's words):** "What determines your worth when everyone tells you you are worth nothing, you are nothing, you are useless, empty and a nobody because you have nothing? In a world where power rules, the weak must follow and obey. But you can choose who you are, you can break free, you just need to do it, give it your all."
- **"Give it your all"** was a way of putting it, not a literal rule. It is both the lesson and the mistake.
- **Ending direction:**
  - The tear still happens, in some form, and thousands of people die.
  - **Where and when:** Favale, on the Longest Light. The lore around it (event names, characters, everything else) will change when we reach those chapters.
  - **Cause.** The tear comes from Seralune, but because of something Alaric does. She didn't want it to happen. "The person who has nothing, trying to be a better person, is the one who does it."
  - **Blame.** People think it was her, and hate her, without knowing the actual reason.
  - **Seralune reaches for him** at the tear, but with different imagery from the current Chapter 30. To be discussed when we get there.
  - **Knowledge.** No one knows at first that Alaric's action caused it, not even Alaric. "That is the mystery and the sad thing." He feels it was his fault anyway.
  - **Aftermath.** He must question himself and find answers on how to live with this.
  - **The moment itself.** His headspace feels unstable. He feels power inside him release, then sees mass destruction.
  - **His evidence.** Keep "It stopped at you" or equivalent evidence. At that moment, make it emotional: an internal war monologue, "Why did this happen? Why did I do it? Why me, when I'm empty?"
  - **What the reader knows:** somewhere in between. The reader sees what Alaric does and then sees the tear, but the narration never confirms the link. The reader suspects; no one on the page can know.
- **What Volume 1 is about for Alaric:** he's so locked in on chasing the past, who he *was*, that he doesn't realise he's living right now. He's making a life right now, with friends who care about him.
- **External goal:** he wants to learn *who* he is.
- **The answer he doesn't like:** he finds that he is nothing. The answer he finds *is* nothing, so that's what he feels he is.
- **The act that causes the tear:** he causes it while chasing who he was, alone and on a wrong belief.
- **Through him, not from him.** Seralune is the one who can use his Veiled powers, but he feels it pass through him.
- **The mechanism:** both reach at once. He reaches for his past, she reaches for him, and her power goes through him. Chasing the past is literally what opens the way.
- **What he wins in Volume 1** (27 September): "companions that want to help him grow."
- **His last choice in Volume 1:** he carries it alone. He tells no one what he felt pass through him, and shuts out the friends beside him.
- **End state:** two beliefs that can't both be true: "I am nothing" and "I killed thousands."
- **Volume 1 in the design bible's five phases (agreed):**
  1. *Promise and displacement.* He wakes knowing nothing; Gerolt calls him Empty and dies for him. Goal: find out who he was.
  2. *Rules and entanglement.* The road, the world's cruelty, friends, clues about his past. His working belief: "if I find out who I was, I'll know what I'm worth."
  3. *Reversal.* The past answers him with nothing.
  4. *Doubling down.* Instead of turning to the life he has, he chases harder, and alone.
  5. *Choice and consequence.* The tear passes through him while he chases his past. Thousands die, and Seralune is blamed.

### Added from the handoff (28–29 September)

The author's direction only. The handoff's recommendations for each point are in its §14.2, and its proposed structure is in §19.

- **Length.** The author is comfortable with forty or more chapters, governed by completed movements, not a word count (handoff §4). *The 50–54-chapter, nine-movement map in handoff §19 is a proposal, not approved.*
- **The Great Expanse** can be a substantial middle movement, not a short crossing. It's vast and empty, distorted by corrupted mana: places move, ruined towns and cities break up the land, night is especially dangerous, and people or creatures who try to live there can be warped.
- **Foramen, Kurdag and Liluth.** The hidden settlement is Foramen, the wolf beastman tied to it is Kurdag, and Liluth is the Natharul scout pursuing them. Kurdag understands what surviving in the Expanse costs; illness or corruption among the people who live or work there may show it.
  - Alaric may briefly believe he has found somewhere he could belong.
  - Liluth's pursuit brings violence to Foramen, and residents ask why elves and soldiers are chasing him so far into Mydea. Some want his party gone, because they brought death to people who had nothing to do with it.
  - Alaric increasingly concludes that wherever he goes, people die: Gerolt, then Foramen, then the tear.
  - His companions start asking who he is, and what could make him worth following into the most dangerous region in Mydea.
- **Belonging is the centre.** The author challenged the idea that Alaric's smaller personal preferences should carry the arc. What matters is the travelling group: the *Final Fantasy XV* road trip, where Silas, Redd, Freya and Wena gradually become the place he belongs. His friends can doubt his secrets, or the danger following him, without ceasing to care about him.
- **The ancient cores** were mass-produced about a thousand years ago, in the war against the princess modern history calls evil. A core gives Alaric no ordinary biography and no easy proof of time travel, and present-day people think arriving from a thousand years ago is impossible. He learns almost nothing straightforward about himself.
- **His false responsibility.** As the volume goes on he comes to believe that recovering his identity is his responsibility alone. He investigates, withholds and decides by himself, and that leads to the final mistake: he reaches for his past without his companions and helps cause the tear.
- **At the tear:**
  - The author has considered killing a recognisable child affected by Alaric and his group. *Not locked.*
  - Seralune sees people dead around her.
  - Nereth survives, close to Seralune.
  - Thaeroval is cut off from the centre of the disaster, not standing safe inside it.
  - Atera regenerates from catastrophic injury and feels all of it.
  - Alaric takes the deaths as proof that people suffer whenever he pursues who he was, which pushes him towards isolating himself.
- **Seralune's route.** Cyrandor's Order tells her that her mother left something for her, or wanted her to find a path. She goes into Mydea rather than straight to Favale. Her search may lead first to **Inrandeel**, the enormous rainforest where, in her remembered age, independent elves lived in peace outside Natharul's direct rule. She expects to find them and finds the community destroyed or removed. Their fate raises new questions about her mother, Natharul, her brother and the forgotten history involving Alaric, and something there points her on to Favale.

## Volume 2

- **The question (the author's words):** "In a world full of politics, brutality, war, slavery and death, much like real life, what can you do, even if it's something small, to do better?"
- **The image.** Alaric learns to rely on others to do "good". Seralune learns that choosing for others isn't the right option. She asks Nereth what she wants, and they decide together.
- **The mission.** Darcy is rescued, by Alaric *with* his friends.
- **Alaric's journey.** Coming to terms with himself, and learning to accept help.
- **Freya.** The whole of Volume 2 develops Alaric and Freya's relationship realistically, not rushed.
- **What can never go back by the end:**
  - Alaric and company have crossed Mydea, killing soldiers and stealing the kingdom's strategist. People are truly against them now.
  - The beastfolk are winning on the border and pushing in.
  - Seralune and Nereth, making their decisions together, escape captivity after all the politics.
- **Volume 2 ends** with Alaric and company crossing the sea to Kozmagar, and Seralune and Nereth escaping. The reader knows both groups are heading the same way; the characters don't.
- **Seralune's lesson is only for Nereth, for now.** She learns to ask the person in front of her, not yet the world. That leaves room for her antagonist arc.
- **Stealing Darcy is why the beastfolk start winning** and pushing into Mydea. Their one small good brings the war home.
- **Gilmot's threat doesn't come true.** The soldiers are drawn off to the war, leaving the Faint quarter alone.
- **Alaric and Freya become mutual before Seralune arrives,** late in Volume 2, once Freya stands on her own.

## Volume 3

- **The quote it follows (the author's words):** "Life is not measured by time, it is measured by moments. Some are big, some are small; most of them are small. Life is this way. Savour even the smallest, because that's all there is to it."
- **Where it ends:** the world on the brink of all-out war, with Natharul and Mydea against Kozmagar.
- **The Time bearer** is looking for Alaric.
- **Not slow.** Volume 3 has blood and death. That's what makes people value the small moments: the big ones aren't guaranteed.
- **Sources of blood:**
  - **Mydea's hunters,** crossing the sea after the group.
  - **Beastfolk scouts,** who know of Darcy.
  - **Natharul,** whose hidden aim survives: the war is to kill the Time bearer.
- **Only Wena dies in Volume 3.**
- **The climax (the author's design), which is also Alaric and Seralune's meeting:**
  - The Time bearer and Seralune draw closer to Alaric's location, and Natharul's assassins close in too. Tension rises every chapter until they all converge.
  - Alaric thinks Seralune is one of the assassins, because she's an elf.
  - Wena defends Alaric against the assassins' attack and is hit. Hearing her whimper, Alaric finally breaks.
  - A Veiled Affinity awakens in him, especially because Seralune is right there. He kills all the assassins, then goes for Seralune.
  - The Time bearer and Freya stop him.
  - Wena is dead. Alaric passes out.
- **The power that wakes is Spirit.** It takes the assassins' souls out of their bodies, and they die. (The author is open to doing this better.) The Silent Field's dead were killed by the spell, not by Alaric.
- **The souls go into the Last Dark,** cast outside the Turning, never to return. He does to them what was done to him.
- **Natharul's Hero, the living Spirit bearer, feels his Spirit affinity leave him for a second,** as if it were pulled out of him.
- **Alaric's goal in Volume 3:** still open; the author doesn't know yet.
- **The assassins are elite:** every one of them is strong enough to kill a Time bearer. Silas, Redd and Darcy are overwhelmed.
- **The Time bearer understands only this:** this is who he was searching for.
- **Seralune does not gain a companion in Volume 2.**
- **Darcy refuses to help Kozmagar.** She doesn't want any more blood on her hands.

## Chapter 1

- **Purpose:** it's about him not knowing anything.
- **Gerolt reacts to the dead elves** on his land.
- **An uncorrected wrong belief.** At least one belief he forms in Chapter 1 stays uncorrected; the reader learns later that it was wrong. It's the running figure (below).
- **Why he's shocked when he sees magic:** he has forgotten everything about himself and everything around him. The spell a thousand years ago literally erased his existence.
- **The flame (locked).** During the Affinity questioning, Gerolt summons a flicker of flame in his hand to show the boy. The boy is shocked. He recognises magic "from outside", drawing the resemblance, but knows something is missing inside himself.
  - The boy *thinks* "magic"; he doesn't say it aloud.
  - Gerolt uses his fire every day. It isn't something he has put away.
  - A small, controlled flicker is compatible with him not using fire in a fight until his last stand.
  - **His palm reddens** after holding the flame, and he doesn't mention it or look at it (agreed with revision 1).
- **Revision format.** When the corrected chapter is written, show the author what changed and what was added, each as a before and after.
- **The belief that stays wrong (line 571).** He concludes the running figure was coming to stop him. The reader later learns she was running to reach him. This echoes the Volume 3 climax, where he takes Seralune for an assassin. "*Was I here with them?*" stays a question he can't answer.
- **A deadline.** Gerolt knows that by morning people will come (neighbours, the church, soldiers) and that someone will talk. He never decides what to do with the boy before the riders arrive.
- **Gerolt knows about the secret scout agreement.** It's shown and never explained: what shocks him is that they're *seen*.
- **The sword is planted with one glance** at the floor under the table when the hoofbeats come. There's no explanation.
- **The narration keeps "the boy",** with one age cue restored: Gerolt guesses "twenty winters, maybe".
- **Gerolt's surname stays out of Chapter 1.** "Warde" comes later, from someone who knew him.
- **Revisions 1 and 2 applied and approved (26 September).** Every change is listed with its before and after in `Volume 1/Chapter 1 - Changes.md`. Only change 21 was rejected. The earlier draft is kept in `Volume 1/Drafts/`.
- **Line pass (28–29 September, accepted; handoff §3).** Seven changes, in `Volume 1/Chapter 1 - Changes (line pass).md`:
  - He reopens his eyes before he sees the broad shape over him.
  - A comparison he couldn't make ("the way a man checks a door…") is cut.
  - On the field, the clothes come down to what matters there: no armour, no weapon, no tear. The cloth and the stitching are left to Gerolt in the cabin.
  - "Gerolt forgot about his back" becomes "Gerolt's fist fell away from his back", and "Gerolt read his face and gave up on explaining" becomes "Gerolt studied him for a moment": things the boy can see.
  - "Who made them?" (the clothes), and the figure in the vision is "close enough to touch me".
  - Chapter 1 is now 6,208 words. The handoff's working score is 96/100, and it gets no more general beautification passes.

## Chapter 2

The plan is built in `Volume 1/Chapter 2 - Design.md`.

**Redesign (27 September).** The chapter merged on 26 September is the version before this redesign.

- **The reader should feel shock at Gerolt's death, not grief.** So there's no extra day before the scouts come.
- **Chapter 1's ending stays** ("I like chapter 1's ending").
- **Gerolt lives longer.** The author: "maybe we can make Gerolt live for a bit longer with him and Alaric running somewhere, then Gerolt dies and gives his sword and Wena to Alaric at the end of chapter 2." The handover and his death move from the cabin to the end of the run. The details are being designed in round 5 of the design file.
- **Alaric's thoughts come back** into Chapter 2, in his own words, and we work them out together.
- **The new shape (round 5, answered 27 September):**
  - **The door stays as written.** In the fight, Gerolt *dodges* Liluth's stone instead of taking it under the ribs, then cuts her. "Maybe he is injured as well."
  - **Gerolt sets his own house on fire** as they leave, "knowing there is no coming back".
  - **He leads the riders away from his neighbours.** "Gerolt knows he needs to lead the elves away or they will kill his neighbours, so they both get on the horse outside and run towards the forest."
  - **Alaric part-carries him** at some point (agreed).
  - **The name comes on the run,** at the worst moment, and "There you are" is said with time still left (agreed).
  - **His death comes just when it looks as though they've made it** (agreed). He gives the sword and Wena in a handful of words, and there's no long goodbye.
  - **Silas is there.** The author: "maybe Gerolt makes his last stand in front of a few elves, is shot with a couple of arrows and falls to his knees. Silas comes through and cuts down the remaining riders, and he and Alaric RUN."
  - **What burns:** "the house and some riders on Gerolt's last stand".
- **Round 6 (answered 27 September):**
  - **The wound (agreed).** Thanks to the shout, the spear misses his ribs and tears along his side. Liluth's slab still throws him back and breaks something. The arrows are what kill him.
  - **The house (agreed).** Alaric sees him burn it and doesn't know why. For us, the reasons are "no coming back", and that the fire draws the riders to him and away from the neighbours. His line: "like 'I guess this is finally goodbye', with his Cid sarcastic humour" (being designed).
  - **The carrying happens twice (agreed):** from the cabin to the horse, and in the forest on foot, where the name comes. "Make the carrying difficult: Alaric is still weak and Gerolt is using most of his strength to stand."
  - **Why Silas is there.** "Silas is at the river, he 'stays' there. He heard the elves and the fight, so he came to see what it was, and sees his former master fighting to the death."
  - **Gerolt sees Silas.** "Gerolt is finally on his knees, blood coming out of his mouth, coughing, arrows through him, and then Silas comes. Gerolt lets out a small 'heh' laugh and doesn't say anything again, ever again. After that he is dead."
  - **Gerolt is dead when they run.**
  - **Alaric doesn't run when he's told.** The author's line for him: "PLEASE GEROLT! You can still live, come!!! Come with me please, don't leave me alone, I need answers." "It kind of turns sadness into anger that he has nothing again." (Being designed.)
  - **The last image:** "Gerolt on his knees, dead, as Silas drags Alaric away from the battle."
- **Redrafted (27 September).** The new draft is compared with Version 1 in `Volume 1/Chapter 2 - What the Redesign Changed.md`.
- **The author's notes on the redraft (27 September),** applied as round 1 of `Volume 1/Drafts/Chapter 2 - change list.json`:
  - Cut "Alaric stopped laughing." and "He stayed on his knees." The page still never says Gerolt is dead: the "heh", the fire going out, and the last line showing him kneeling.
  - The neighbours' window stays (call 1: "Yes"), and Gerolt says "The trees…" before "Make for the trees, lad."
  - Wena is shown as Alaric sees her: staring at Gerolt, looking at Alaric, a pause, then running after him.
  - "The dark" cut across the chapter.
  - The other calls from the redraft were answered on 27 September (round 4). Gerolt puts his hand on "the wall next to where the door was", not the doorpost. "I don't like 'I run hot'", so it stays out, as does "Found one lad still breathing". "Everything else I approve": the horse, Gerolt's small lines ("Good.", "Don't haul on them.", "Still here.", swearing "softly and at length"), the horse being shot, Alaric's thought when Gerolt goes down, the riders coming from the river, the rider's laugh, Silas's look (big, a long cloak, a heavy blade, stubble, a pale scar from cheekbone to jaw), Silas's eyes on the sword, and the last line.
- **Round 2 (27 September): "Just add meaning to things."** The author's line after Gerolt dies goes in: "Alaric couldn't get up. He was staring at Gerolt. That old man had taken care of him until his dying breath, and now Alaric was going to leave him there and never see him again." So Alaric's understanding, not the narration, is where Gerolt's death is said. Also "The man was at his side before Alaric had noticed him move", and "spattered the ground". Eight more moments with meaning added wait on the author.
- **Round 3 (27 September): the answers on round 2.**
  - Accepted: "Nobody was coming.", the laugh ("none of it was funny"), and "away from Gerolt".
  - The sword gets the author's meaning: he watched Gerolt fight with it, and giving it away means Gerolt will face them with his bare hands and die. Alaric doesn't know what Gerolt's fire can do.
  - "He couldn't leave Gerolt alone with them" ("down there is weird").
  - "Alaric waited for the fire to come back. It had kept burning through both arrows, and now it was out…" ("what is it, give meaning to it").
  - The house is toned down ("too melodramatic"). "Bracken" is gone, and so is "ferns".
  - The eight cuts from round 1 are accepted ("I agree with all the cuts"). Change 26 kept ("Keep 'he wasn't moving'"), with "ferns" removed everywhere ("I don't like 'ferns'"). The house line is rejected (change 25: "I feel it's too much"), so the house burns without comment. Nothing in the change list is waiting on the author, and every call on the redraft is answered.
- **Final pass (27 September),** round 5 of the change list: craft fixes only (two unclear pronouns, repeated words, and "eaves", "pommel" and "sidled" swapped for common words). Merged into main the same day.
- **Final pass of Chapters 1 and 2 together (27 September).** Read as one piece: continuity across the seam, what Chapter 1 set up and Chapter 2 does, phrases repeated between them, and the new rules applied to Chapter 1. Continuity holds all the way through, including the torch, bench, blanket, coat, stool and mug, sword, hearth, shutters, the neighbours, "the questions can wait" and the vision. Three findings:
  - Chapter 1's cabin "Boy?" becomes "Lad?", to match "Gerolt says 'lad', 'boy' is Silas's word". Gerolt's "boy" at the field stays, since the boy is a stranger there. *(Accepted: "I agree with everything you said.")*
  - Chapter 2's "before he could stop it" becomes "The rest spilled out of Alaric", because Chapter 1 uses the same stock phrase (craft fix).
  - Chapter 2 adds the boy's thought *Natharul.* when he first sees the living elf, bringing Gerolt's "They ask where" to the door. *(Accepted: "I agree with everything you said.")*
- **Chapter 1, revision 6 (27 September):** "the dark" taken out five times, at the author's request.
- **Lines agreed (27 September).** The author gives the line in their words, and Claude gives it back in the character's voice.
  - **Gerolt at the house:** "Well," he said to the house. "Suppose that's goodbye, then." The author chose this over a joke about the shutters: "A is better, more human-like. B sounds robotic."
  - **Alaric refusing to run:** "Gerolt! Please, you can still get up. I'll carry you. Just come *on*!" / "Don't leave me on my own. I don't know anything. I don't know *anyone*—" / "You said the questions could wait! You *said*—" / "Don't you dare leave me with *nothing* again!" The author: "emphasise 'nothing'."
  - **His death:** the narration never announces it. Alaric sees the "heh", then the fire on Gerolt's hand goes out, and it lands in his own understanding: "That old man had taken care of him until his dying breath…" (the author's line, round 2). ("He stayed on his knees" was cut on 27 September: "The reader knows he is on his knees.")
  - **The ride:** "Make for the trees, boy," with Wena running alongside.
  - **The name:** the approved exchange stays. At "There you are", Gerolt gives a small pained chuckle: "he is happy but in pain".
  - **The handover:** the sword and Wena in a handful of words, one line sending him to Marta in Kelmend, then "Take Wena and run, Alaric."
  - **Silas's first words:** he's "shocked and kind of annoyed this boy won't get up". The author's line: "Get up, boy, or we're both dead!"
  - **The "made it" line:** "That was the worst horse I ever had, ah haha, slow as shite." "He is laughing at the situation."
  - **"Lad" and "boy":** Gerolt says "lad", and "boy" is Silas's word (agreed).
  - **Alaric's thoughts (the author's rough versions):**
    - At the shout: "He thought that was it, that was all done, everything he has known, even if just in this moment. He would be alone and be nothing again."
    - On the ride: "Why are they attacking us, what just happened, why did Gerolt kill that man, why, what is happening."
    - At the last stand: "What do I do, I can't do anything, I want to help, I can't, I'm scared to help, I will die, I don't want to die." *(Since the line pass, one line; see below.)*
- **Line pass (28–29 September, accepted; handoff §3).** Ten changes, in `Volume 1/Chapter 2 - Changes (line pass).md`:
  - **The elf at the door:** "Open the door, farmer. Keep us waiting, and yours won't be the only one we knock down tonight." It replaces the author's own example line (below, under Version 1).
  - The choking is compressed where sentences repeated the same physical failure.
  - The ride loses its last thought (*What's happening? What is* happening*—*).
  - **At the last stand** Alaric tries to move and his body fails him, instead of only explaining in his head that he can't act. His thought is now *If I go down there, they'll kill me. I don't want to die. I don't want to—*
  - The author's round-2 line is trimmed: "Alaric couldn't get up. Gerolt had taken care of him until his dying breath, and now Alaric was going to leave him there and never see him again."
  - Chapter 2 is now 4,656 words. The handoff's working score is 94/100.

The decisions below were made for Version 1. They were checked against the redesign on 27 September: most still hold, and the ones the redesign replaced are marked *Superseded*.

- **Whose eyes, and the ending.** The whole chapter is in Alaric's eyes. *Superseded ending:* it no longer ends on the cabin burning. Gerolt sets the cabin alight mid-chapter, and the chapter ends with Gerolt kneeling, dead, as Silas drags Alaric away. (Version 1: it ends on Gerolt's cabin going up in flames.) Old Chapter 3's opening ("the night went orange") moves into Chapter 2. *(Claude's proposal, which the author's answer implies: the last he sees of Gerolt is his hand catching fire as he turns to the door.)*
- **The name returns,** and Gerolt says it back before he sends him away. Gerolt must sound like Cid.
- **He breaks his silence** to warn Gerolt about the stone. It saves Gerolt for the moment, and the escaping scout hears it.
- **The fight is explicit and grotesque,** as a boy sees it. The first elf chokes on his own blood. Gerolt cuts the female scout apart with the sword.
- *Superseded:* Gerolt still keeps his fire away from the boy, but now he burns his own house once the boy is outside, and uses fire in his last stand at the river. (Version 1: **His refusal to leave is what holds Gerolt's fire back.**) "Fire is dangerous and Gerolt does not want to harm the boy." It's never explained on the page, and Alaric doesn't learn it in Volume 1.
- **Shape.** *Superseded:* now six movements (the door, the fight, the fire, the ride, the forest, the last stand), still with no `---` breaks. (Version 1: four movements, each ending on an image: the door, the fight, the farewell, the wheat.)
- **Gerolt's voice.** Dry to the end, like Cid: orders instead of feelings, playing down his wound, never saying he cares. His humour drops once, at the name. The old lines are kept or cut as the table in the design file recommends.
- **Kelmend and Marta.** Gerolt sends him west across the river, to Marta at the inn by Kelmend's south gate. The sword is the proof.
- **The neighbours.** The elf threatens the other households. Gerolt hears it, looks at the boy, and picks up the sword. Nobody says what that choice costs, and the neighbours' fate is left for a later chapter.
- **The elves are cocky and full of themselves.** The author's example: "Farmer, answer this damn door before we start knocking down others because of your silence." *(The line itself is superseded by the line pass: "Open the door, farmer. Keep us waiting, and yours won't be the only one we knock down tonight.")*
- **"Empty" as a name: reversed after the first draft.** Gerolt never calls him Empty in Chapter 2. The line is "You're a stubborn little bastard." ("I like it, remove Empty").
- **Where the name comes from.** It arrives through Chapter 1's vision, and this time he hears the word the running figure's mouth was shaping. The author likes the reaching hand and the mouth. The author doesn't like the gold at the cuff, so there's no gold in Chapter 2, and it has been taken out of Chapter 1 as well (revision 4, changes 50–52).
- **Two moments at once.** During the name vision the cabin shows two moments together (the door whole and shattered, Gerolt unhurt and bleeding). It's trimmed to two or three images and never explained.
- **The scouts.** The male dies by the sword through his jaw, choking on his blood, and Alaric never learns his name. Liluth is cut apart (her eye, her face, her arm) and escapes. She heard him, and she returns later in Volume 1.
- **The name Gerolt swallowed** stays unsaid. He dies without saying it, and it's a thread for later.
- **Echoes of Chapter 1**, each used once: THOOM as the name arrives; his left hand opening towards the figure's hand; the stool and mug in the wreckage; the hand of fire answering the reddened palm; the boy saying "I've got you" back to Gerolt as he presses on the wound.
- **Title:** "The Price of a Voice".
- **Answers on the first draft's calls** (26 September):
  - The elf laughs as he steps in: "Testing my patience, old man. Now you've no door to answer." He calls Gerolt "old man" before he has seen him.
  - Kept: the candle line after the wind; the sword skidding to the boy's hand; the torn-off coat and the shirt on the wound. The last line ("perfect") is *superseded* by the redesign's ending.
  - "Tell her the old fool sent you" now ends in a small cough, with blood starting at the corner of his mouth.
  - Cut: "Took you three tries to sit up at midday."
  - *Superseded:* "I run hot" is cut from the redesign ("I don't like 'I run hot'"). (Version 1: the hot hand, which Gerolt covers with a dry line, "Careful, lad. I run hot.") (The author's note: the old narration "doesn't sound like Cid speaking, sounds like a computer monologue.")
  - Kept: the second scout's laugh before we see her.

## Chapter 3

The plan is built in `Volume 1/Chapter 3 - Design.md`.

- **Seralune comes in with Chapter 4,** which is all hers: "Yes, we can make Chapter 4 all Seralune." Chapter 3 stays in Alaric's eyes. *(Settled in Chapter 4, round 1: Chapters 4 and 5 are both hers, and Chapter 4 is the whole day in the seal, from the moment it broke.)*
- **The centre of Chapter 3 is Alaric's inner fight.** "He thinks he is the reason Gerolt is now dead. He is not in a good headspace this chapter." His questions start: why are the elves trying to kill him, what was that war on Gerolt's farm, what is happening.
- **Silas grounds him:** "snap out of it for Gerolt's sake, and keep moving forward for Gerolt's sake and Wena's."
- **The river.** The bridge is broken and the current is strong. Wena still tries to go back to Gerolt, and Alaric grabs her fur and drags her. Silas says to leave the dog; Alaric doesn't.
- **Silas kills one more elf** on their heels, brutally, with his Affinity.
- **Silas's cave:** "covered behind thick bush. It's small, dirty and ugly, and just has the necessary stuff to survive."
- **In the cave,** Silas gives only his name and asks the questions: how Alaric knew Gerolt, why the elves are after him, what happened before. Alaric is angry with him, and brings up that Gerolt told him to go to Marta.
- **Kelmend:** Silas says it's no good, because the guards will hand him over to Natharul without question, so they need to find a way in. This comes after he hears "Marta".
- **Round 2 (27 September).**
  - Alaric ends the chapter still believing Gerolt died because of him. Nobody corrects it, and Silas never says it wasn't his fault.
  - **The kill:** a horse closes in. Silas cuts the horse down, and the rider is left winded on the ground. Silas walks to him slowly and stabs him through the chest, heating his sword and burning him.
  - **What Alaric tells Silas:** waking up knowing nothing, Gerolt giving him food and comfort, the riders, and Gerolt killing one without hesitating and maiming the other. He says it sitting on the ground, hands over his face, in shock.
  - **The ending:** "Marta", Silas's reaction, and "Kelmend's no good". Then Alaric, alone with Wena, cries at last.
  - The neighbours are left out of Chapter 3.
- **The lines (27 September),** designed together. The author gave rough versions and notes; the final wording is in `Volume 1/Chapter 3 - From the Old Chapters.md`. The river has no thought from Alaric ("Alaric isn't thinking here, full of adrenaline"), and Silas hauls them out "swearing the whole time". "Empty" isn't talked about yet.
- **First draft written (27 September):** `Volume 1/Chapter 3 - The Weight of the Living.md` (1,896 words, working title).
- **Round 1 (27 September).**
  - **The bridge** isn't broken: "guards from Kelmend watch it, but an elf rider is already there speaking to the guards".
  - "*It's me. They're coming for me.*" is cut: "How does he know they are coming for him?"
  - **Behind his hands** is a picture of Gerolt well, and seeing Silas "would make reality set in".
  - The author asked whether to add anything. Claude kept the length and proposed three small additions: a glimpse of Silas's grief, Silas not having heard the battle either, and the chasing rider coming from the bridge.
- **Round 2 (27 September).**
  - **The bridge:** "no hut, no lantern". The guards stand round a small fire, chatting, with the rider among them speaking, in joined-up sentences.
  - **Accepted:** Silas's grief glimpse (he doesn't let go of the sword straight away), and the rider from the bridge.
  - **Silas doesn't believe him:** "A battle that size on Gerolt's farm would be the talk of Kelmend, boy, and there wasn't a sound last night." He's "struggling to believe Alaric's answers".
  - Point-of-view fixes: while his eyes are covered or down, Alaric only hears.
- **Round 3 (27 September).**
  - Silas in the river: "—stupid little prick, should've listened to me—", then a snarl.
  - "He didn't care to ask for Alaric's." *(Superseded by the line pass: Alaric waits for Silas to ask his name, and Silas starts cleaning his blade instead.)*
  - "Already" is gone from "looking at the fire".
  - **The ending:** he strokes Wena's head, cries, and whispers "I'm sorry" to her. It's meant for Gerolt as well, and nothing on the page points at it.
  - Everything else from the draft's list is approved ("everything else is fine"), including the title "The Weight of the Living".
- **Final pass (27 September),** round 4: craft fixes only. Nothing is waiting on the author.
- **Final pass of Chapters 1–3 (27 September),** before merging.
  - Read as one run: continuity across both seams, the rules added since each chapter was finished, phrases repeated between chapters, and the records.
  - Fixes: two "already"s Alaric couldn't know, one in Chapter 1 ("to find Gerolt watching him") and one in Chapter 2 ("He was looking at the horse"). Chapter 3 no longer repeats two phrases from Chapter 2 ("broke out of the trees", "set his feet").
  - Stale notes are resolved here, and in the Volume 1 picture.
  - Lengths: Chapter 1 is 6,284 words, Chapter 2 4,723, Chapter 3 1,990.
- **Round 6 (27 September).** Two of Alaric's thoughts are joined into single lines. "*If I stop, then he—so don't, idiot. Move.*" uses Silas's own "move". "*They've already killed him—what more do they want? Why are they still chasing me?*" stays a question, so it claims nothing he couldn't know. Chapter 3 is now 1,995 words.
- **"The man is said too much" (27 September).** In Chapter 3 it was said 22 times before Silas gives his name, and now 8, plus "the stranger" twice. The rest became "he" where only he can be meant, "a fist" or "a hand" where that's all Alaric feels, or were cut. The end of Chapter 2 lost a sentence that said it twice. *(The line pass brings it back to 10.)*
- **An outside review (27 September).** The author pasted a five-point review of Chapter 3. Nothing in the text changes. Two notes carry forward to later chapters (Claude's reading; the author moved straight on to Chapter 4):
  - **Pay a small answer on Silas, Gerolt and Marta soon,** most naturally when Marta sees Silas at her door. "Marta." said to the blade is a strong tell, and readers will be waiting.
  - **Next time Silas is on the page, he shouldn't win cleanly.** He has now shown he's capable three times running. His flaws are decided ("acts instead of thinking", "reckless in the big choices"), and Marta can shake him.
  - Answered against the review: "Then Gerolt died for nothing" stays, because Gerolt's death is decided and Chapter 2 already says it. "Stop drowning in self-pity" stays, because it's the author's line, meant to be harsh, and Alaric's "*Move*" echoes it. *(Superseded by the line pass: see below.)*
- **The title** is "The Weight of the Living". It was briefly "I'm Sorry" on 28 September and restored the same day, because "I'm Sorry" was too narrowly tied to the closing line (handoff §1).
- **Line pass (28–29 September, accepted; handoff §3).** Seven changes, in `Volume 1/Chapter 3 - Changes (line pass).md`. Before it, Chapter 3 was the weakest of the four, because Silas withheld both his history and the ordinary reason he was near the farm. His history stays hidden; his arrival now has a cause.
  - **Silas grounds him:** "They'll be hot on our trail soon enough, boy. Get up and move, or Gerolt died for nothing." It replaces "Stop drowning in self-pity, boy, and move" and "You want to die? Fine…".
  - **Silas's accusation:** "And you had his sword in your hands, but you stayed where you were and did nothing," he said quietly. It replaces "like a scared little puppy".
  - **His name:** Alaric waits for Silas to ask his name. Silas doesn't; he starts cleaning his blade. It's observed, never explained as proof that Silas doesn't care.
  - **Why Silas was there:** Alaric asks how he knew Gerolt, and Silas answers a different question: "I heard something from across the river. Sounded like fighting, and by the time I got close enough to see what was happening, it was already too late." / "That isn't what I asked." / "No, it isn't." The rag moved along the blade. "How did you know him?"
  - **The river:** "The river turned him round, the bank went past, and then a fallen tree lying out into the river from the far bank, close enough to touch."
  - Chapter 3 is now 2,026 words. The handoff's working score is 92/100; the opening four together, about 95.

## Chapter 4

The plan is built in `Volume 1/Chapter 4 - Design.md`.

- **Round 1 (27 September).**
  - **Two chapters, not one.** "Both Chapters 4 and 5 must be her chapters; 6 can return to Alaric." They cover "her leaving her seal, and all the lore around Natharul leading up to Cyrandor". "These chapters must be better than their predecessors and rely on my image of world building."
  - **Chapter 4 is the day in the seal.** "She is exploring this dark room, completely black, fighting with her Alisaie inner monologue: thinking if she is dead, how did she end up here, what is happening. She must explore all emotions. It's a full day of nothingness."
  - **It ends on the old image:** Thaeroval at the door, and Seralune seeing fear in her brother's eyes for the first time ever.
  - **Not told "sealed" yet.** "Revealing 'sealed' right now is too soon. She should put the pieces together." Thaeroval deflects: "enough of the questions, come, follow me, do this, do that."
  - **Her voice** (agreed): Shoko with Thaer at first, turning Alisaie as he shuts her out; Alisaie with everyone else from the start. She says sorry. *Superseded in round 2:* the counting in Thaer's voice ("Count. One breath first."), and the sorry "when her mana flares", since it no longer flares.
  - *Claude's reading, not objected to in round 2:* "Yes" to question 2 also accepts Thaer feeling the seal break and coming from far off, which is why no one comes all day, and the reader learning she's an elf from the point of his ear.
- **Round 2 (27 September).**
  - **Chapter 5 ends on the two knocks** at first light, with Cyrandor unseen behind the door. Her escape is Chapter 7, after Alaric's Chapter 6.
  - **Chapter 4's order is approved,** with two changes. "I don't like the counting, remove it." And when she goes back through her last day, it's her mother and Thaer only: "not Elowen yet".
  - **The crystal:** yes to Claude's suggestions. It split open around her, and she wakes on the floor among sharp pieces, in a stone room with a door that has no handle on her side. She feels the break: her mana rushing out towards something far away and finding it, then the crack and the white. Afterwards the broken crystal still pulls at her mana.
  - **What she works out** (agreed): many years have passed, and the crystal was made for her. Nobody says "sealed" or "a thousand years". The number and her mother come from Cyrandor in the escape, the first person who answers her instead of giving orders.
  - **Cyrandor's first sight of her:** "a mix of both" (the old bow, and keeping him off the page). *Settled in round 3:* he bows and smiles, and there's no special old bow.
  - **Seralune snaps at Nereth, and her mana doesn't flare** (the author): "Seralune is getting angry at no one telling her anything and snaps at Nereth. The guards charge in thinking something bad is going to happen, but Nereth steps between them, saying she is just tired and needs to rest", because of Cyrandor's order.
  - **The blows under the floor** all night are the crystal being repaired.
- **Round 3 (27 September).**
  - **Chapter 5's order holds** ("Yes, it holds"). See `Volume 1/Chapter 4 - Design.md`.
  - **"Ask me":** the author's version is "I'm standing right here, you know, just ask me", "something like this".
  - **Through the door.** "The king took the royal battleship in the sky; a rider can't catch up." Leorin "just says the king must be told at once, take her into custody and prepare the seal". Thaer gets angry: "no one touches my sister until I say so", "something like this".
  - **Why Thaer gives orders:** "He wants to get her away from prying eyes, and in a place he thinks is safe, so he can do other things."
  - **The city** is inside the forest, "like Oriflamme" (FFXVI). The sound of the falls is the first thing she knows when she comes up.
  - **Cyrandor bows and smiles a little.** In her head: she has never seen him before, and he is the first person who has smiled at her, when everyone so far looks worried and scared.
  - **Her sorry to Nereth,** once the guards have gone: yes.
  - **Her thinking is Alisaie's.** The author pasted Alisaie's lines from FFXIV (on saving Ga Bu) as the model for her inner voice: she reasons her way forward, is sure of her conclusions, and turns straight to the next practical step.
  - **The end of her talk with Thaer:** she doesn't say "I trust you". "No, she is angry with him, how Alisaie fights with Alphinaud."
- **Round 4 and the line notes (27 September).** The lines as they now stand are in `Volume 1/Chapter 4 - Design.md`.
  - **She overhears "the seal".** This changes round 2's "she doesn't have the word yet". She hears it through the door and asks herself: "Seal? What seal, why are they preparing a seal? Is that the room I was in?" Nobody says it to her face, and nobody tells her why.
  - **Ships in the sky:** "Yes, if you read Chapter 13 or 14 of the old stories, there is the airship there." The look comes from old Chapter 13: an immense armoured body of overlapping plates, a ribbed underside with blue-green light running through it, and a deep hum.
  - **Her last memory is "this morning"** (the author): "Mother was in my room this morning, I forgot what we fought about, and Thaer was there promising to be back before evening." The pears are gone.
  - **Her thought about Thaer** isn't that he's giving her orders, but "why is he acting so stressed? He has never been like this before."
  - **No explaining in her thoughts.** "That tree hasn't grown a hand's width in my whole life" was "against chapter rules, explaining things like a hand's width, doesn't make any sense". It's now "How in the world did the tree grow so big? Yesterday it was way smaller. How long was I in that room?"
  - **Her snap must break.** "You couldn't say. Of course you couldn't." "sounds weird": make it one sentence, "Of course, no one can say anything." And "Were you told to stand there…" "doesn't sound angry at all. Seralune must break here, like 'ARRGHH, WHY CAN'T ANYONE JUST SAY WHAT IS GOING ON!?'"
  - **Her anger at Thaer,** in the author's words: "You told me to follow you and I did, you told me to rest and I did, I waited, and now I want answers, I want them now." / "I'm not a child any more, Thaer, I want to know what is going on." / Thaer: "Seralune, get some rest, I will be back in the morning."
- **Round 5 (27 September).**
  - **The airship she sees is the royal warship itself, leaving** (agreed). Ships in her time were "smaller, not this big": "not in her time, 1000 years ago".
  - **The fight with her mother she can't remember is a hole where Alaric was:** "Yes." It stays unexplained on the page.
  - **"You said you'd be back before evening, too."** Keep.
  - **The first draft of Chapter 4 begins:** "begin the chapter".
- **First draft written (27 September):** "Before Evening" (2,651 words, working title; now saved as `Volume 1/Drafts/Chapter 4 - Before Evening (Draft 1).md`), compared with the old coda in `Volume 1/Chapter 4 - From the Old Chapters.md`. It has eight calls for the author: the scream in the white, the silent falls, how her mana feels when she's frightened, Thaer's knocks and the cut door, "He smelled of horses", the crystal's inside pulling, the length, and the title.
- **The accepted chapter (28–29 September).** Outside this repository, the draft became `Volume 1/Chapter 4 - A Promise Left Fractured.md` (2,626 words), accepted by the author (handoff §3). Only five things changed, listed in `Volume 1/Chapter 4 - Changes.md`: the title, one of her thoughts, the line where her voice comes back to her, a stress mark, and "He smelled of horses" (cut). So of the draft's eight calls, "He smelled of horses" was cut, the title changed, and the other six stayed as drafted.
  - **Title: "A Promise Left Fractured"** (28 September). On first reading it seems to be about Thaer's promise to be back before evening, and the broken crystal round her. Its hidden meaning is the promise ancient Alaric and Seralune made to stay by each other's side, which other people fractured when they separated them, leaving her unable to remember him. That promise's wording and circumstances aren't written yet, and should get a full scene of their own later rather than stay background lore.
  - **All Seralune, and quiet.** Her first day alone in the broken crystal chamber. The threat is confinement, thirst, uncertainty, time and the chance that no one is coming.
  - **It opens on the rupture** the author prefers: her mana leaves her for the first time in her life, takes hold of something far away, and "Everything around her cracked. The sound went through her teeth and into her bones, and someone was screaming, and it was her, and the whole world went white."
  - **It ends when Thaeroval reaches her.** He cuts the door open; she runs into him expecting safety; his arms don't close round her; he stares past her at the crystal; and for the first time she sees fear in her brother's eyes.
  - **Mana and 『Affinity』 are different words on purpose.** Mana is the fuel. An Affinity is the force or element that shapes it. Seralune has limitless mana and no Affinity. "Magic" is her age's word, from before the modern laws made "Affinity" the usual one. So she speaks of mana and magic without contradicting Chapter 1.
  - **Her thoughts** come often because she's alone. Each one should change what she understands, how she feels, or what she does next. The handoff found no viewpoint slips.
  - **What the chapter puts on the page is canon** ("Yes", 29 September). Most of it was already agreed in rounds 2–4 above:
    - She has always been able to hear the palace falls (round 3).
    - Thaer knocks twice and never waits to be let in (old canon; the knock returns in Chapter 5).
    - The crystal is hollow, with an opening taller than she is, and when she reaches inside it draws her mana out of her, slow and cold, until she tears free (round 2).
    - The chamber door has no handle, latch or keyhole on her side (round 2).
    - Her last memory is of fighting with her mother "this morning" (she can't remember a word of it), then Thaer promising to be back before evening (the author's line, round 4). The fight is a hole where Alaric was (round 5).
    - She wakes barefoot, her hair loose, in the dress from what feels like the day before (handoff §6.2).

## Chapter 5

**Its order and its lines were agreed on 27 September,** in `Volume 1/Chapter 4 - Design.md` ("Chapter 5, the order", approved in round 3, and "The lines, version 2"). It runs from the embrace in the chamber to first light, and ends on the knock, with Cyrandor unseen behind the door. Her escape is Chapter 7, after Alaric's Chapter 6.

**The handoff adds** (28–29 September). Where it changes the agreed design, the design is now being worked through in `Volume 1/Chapters 5–10 - Design.md`.

- **It may be split into Part One and Part Two** rather than rushing its revelations (handoff §14.2).
- **Seralune's state** (handoff §15.2). She remembers being a princess yesterday. She wakes to people who are frightened of her, evade her questions and may be deciding what to do with her. She is confused, alarmed and distrustful: what happened, why will nobody answer, why are they afraid of her, what are they planning? She doesn't meekly accept explanations, or act as if she has already adjusted to the present.
- **Cyrandor's knock is different from Thaer's.** Seralune is so caught up in what happened, and in what Thaer might say, that she first assumes it's Thaer at the door (handoff §14.2). *This changes the agreed ending, where the knocks were "spaced exactly like Thaer's".*
- **Thaeroval regrets the ancient sealing** and hopes their father may also change his mind. He doesn't want to reseal her straight away, and delays while he holds on to that hope (handoff §14.2). *This changes "stays exactly as written"; see Thaeroval.*
- *Open:* her first active choice, and what each part's dramatic question is. Nereth's first disobedience ("still undecided", handoff §15.10).

## Alaric

- About twenty.
- **Personality.** Still himself without knowing who he is: kind, smart and caring. He wants to help those around him, and isn't afraid to take action, even if it means killing someone. He doesn't know that about himself yet.
- **References:** a mix of Subaru (Re:Zero) and Alphinaud (FFXIV).
- **Flaw.** He thinks he can carry everything alone and wants to take on everyone's burdens. Early on he can be a bit immature because he's young. He learns from terrible mistakes, grows as a person and learns to rely on those around him.
- **His immaturity in Chapter 1:** because he knows nothing, he believes things are right when they aren't.
- **Memory rule:** he knows what things are, but has never experienced any of them. This is never stated on the page (see Principle 3).
- **When he's frightened: Subaru's mouth** (27 September). The author: "like omg what was that, what must I do, I'm a weakling, I can't do anything, omg omg."
- **His habit** (27 September): "he likes to think a lot and keep emotions to himself instead of asking others for help."
- *Claude's reading, to confirm:* the two fit together if the mouth runs inside his head and he keeps it shut outside. It spills out loud only when he's cornered, as in the Chapter 1 rant ("that is the whole list, Gerolt"). His panic keeps Subaru's shape (fast, repeating, calling himself useless) in words from his own world, since he isn't from ours.
- **He isn't the ancient Alaric** (handoff §15.5). He begins blank and can choose who he becomes, even while he searches obsessively for who he was. The ancient promise doesn't bind him, and he owes Seralune no romance because of the past.

## Seralune

- **Core (the author's words):** "a stubborn princess who stands up for herself and never backs down from what she wants." She's a bit of a tsundere (when she loves Alaric). She's never cocky, and she says sorry. She has emotions and cares deeply for those around her.
- **References:** like Alisaie (FFXIV), but more like Shoko Nishimiya (*A Silent Voice*).
- **When each shows:** Alisaie in everyday life. Shoko when she is with someone she's extremely comfortable with.
- **The twins are deliberate.** Alaric takes from Alphinaud and Seralune from Alisaie, his twin, to show their connection to one another.
- **Flaw.** She's very compassionate, which makes her want to help everyone, be friends with everyone and have the best image. Because of this she often takes control of situations, and they end badly. She needs to learn that people must choose for themselves, and that her way isn't always the only way.
- **Her side of the volume's question.** She is told she was sealed for her own good. She doesn't remember it, or making any decision for herself, so it scares her and she rejects it.
  - **Not in Chapters 4–5** (27 September): "Revealing 'sealed' right now is too soon. She should put the pieces together."
- **What she wants (the author's words):** "a world where people don't have to fear those with nothing, or herself." "A world where people don't have to choose what they want, because they have everything they need."
- **Her wish is deliberately the seed of her antagonist arc.** She wants to choose for others. People don't want that; they want their own freedom of choice.
- **Volume 1 goal.** She wants to escape a system that is choosing to lock her away because everyone tells her she's dangerous. She knows she isn't: she's a kind person who just wants to help everyone. Her mother opposed her sealing, and she wants answers on why they sealed her, directly from her mother.
- **Her belief across Volume 1.** At first she thinks, "How could I be dangerous? I never had magic." She says "magic" because she knows the word from a thousand years ago. People around her accuse her. Then her own actions endanger people, and she starts to believe she is the problem.
- **Volume 1 breaks her into something dangerous.**
- **Her mana.** She knows she has mana, and a lot of it. Everyone believes it's simply a very large pool: no one has been able to find its end. In truth it has none.
- **Her mana.** She knows she has mana, and a lot of it. Everyone believes it's simply a very large pool: no one has been able to find its end. In truth it has none. *Now in question (handoff §14.5): a world that is fading because its energy is running out sits badly with a reserve that truly never ends. See Open questions.*
- **A rule: her mana can't be used** (27 September). "Her mana isn't usable at all, nor should she think it is. It is only usable through Alaric. Her mana just exists within her." So she never tries to shape it, and never expects to.
- **But it acts on its own** (27 September): "Yes, her mana acts on its own." That's how it went searching for Alaric, and how her feelings make Nereth's corruption flare.
- **She isn't the ancient Seralune either** (handoff §15.5). She keeps the princess-self she remembers but has no memory of Alaric, and owes him nothing because of a past relationship.
- **Her last choice in Volume 1.** She accepts responsibility for who she was, even though that isn't her true self and she didn't actually do those things. Her internal war: "I need to atone for all these deaths. But was it me? Why must I? But I should."
- **Where Volume 1 leaves her:** she and Nereth are held by the Holy bearer. The church keeps her alive as leverage over Natharul.

## Gerolt Warde

- **Name.** Full name Gerolt Warde. The echo of "ward" (Alaric was the queen's ward) is not deliberate.
- **Affinity:** Fire, Eminent, the same level as Liluth.
- **Life.** A farmer, retired from fighting and passing his days in his own company. He was a hardened man, but has had enough of this world and wants peace. He lives alone because he wants to; he likes peace with just Wena.
- **Readiness.** He's out, but he still has a war underneath that he's always ready to face.
- **He was in Avarice.** He taught Silas there, and was angry that Silas didn't learn from his teachings.
- **From Cid (FFXVI):** a mix of the humour and the damage underneath.
- **His fear.** He knows what people do to those with no magic, and he's scared the boy won't survive in this world, on top of the boy knowing nothing about himself. He can't shelter him because of what would happen, but he doesn't want to harm him either.
- **Why he doesn't use fire until the end:** magic can have negative effects, and he doesn't want to hurt the boy or destroy his house.
- **Death:** he still dies in Chapter 2, with a hand of fire, ready to use his Affinity in a last stand. *Redesign (27 September):* the stand is now in front of a few riders, away from the house. Some riders burn, then he's shot with a couple of arrows and falls to his knees, and Silas arrives.
- **He burns his own house** (27 September), "knowing there is no coming back". It's the first time the boy sees his fire used in full.
- **The sword:** instead of the token, Gerolt gives Alaric the sword he's been using. It's memorable, and Alaric can use it in the future.
- **How he lives (agreed with Chapter 1, revision 1):** one bowl, one coat, one bed, and he gives the bed to the boy. He sets his stool where he can see both the bed and the door.
- **Natharul.** He names them out loud at the window ("They ask where"). When the riders arrive, the name he starts to say and swallows is something more specific that he recognises. He dies without saying it (agreed for Chapter 2). *What that name is: open, for later.*
- **Sending him away:** in Chapter 2, as he's dying, to Marta in Kelmend, with the sword and Wena (confirmed 26 September). This still holds in the redesign: at the river, "Kelmend. Over the river. Marta, at the inn by the south gate. Show her that. Tell her the old fool sent you."

## Marta

- **Gerolt's niece** (agreed 26 September, for Chapter 2). She keeps the inn by Kelmend's south gate.
- **Her father was Gerolt's brother,** and he died in Silas's gorge. That's part of why Gerolt is angry with Silas.
- Everything else about her is still to be decided.

## Thaeroval

- **Everything from the old version survives,** and he stays exactly as written. His entry in `Old - Before Re-plan/World Bible/The World.md` ("Thaeroval — Seralune's Elder Brother / First Blade / Dark Bearer") is the reference. *Changed (handoff §14.2):* he regrets the ancient sealing and hopes their father may also change his mind. He doesn't want to reseal her straight away, and delays while he holds on to that hope.
- **What he wants in Volume 1:** his sister safe in his "chains". He believes he must choose for her the best way to keep her safe, and that is resealing her.
- **The seal** (27 September): "Thaeroval sealed her in a massive crystalline structure that contained her mana and used it against her to keep her sealed. When Alaric appeared, the mana searched for him and cracked the seal." It's intentional that she wakes because Alaric appeared.
- **How he answers her** (27 September): he doesn't. "Enough of the questions, come, follow me, do this, do that." Why: "He wants to get her away from prying eyes, and in a place he thinks is safe, so he can do other things."
- **He spares Alaric.** He's far more interested in reaching his sister than in doing anything to a boy who means nothing compared to her.
- **When he passes Alaric he feels literally nothing.**
- **His erosion.** He slowly loses his emotions until he becomes flat, but that happens much later in the series.

## Natharul's palace

Agreed for Chapters 4–5 (27 September). Who each person is gets decided with the author when they're on the page.

- **Leorin** is the author's own character. He's Seralune's cousin, and "he looks extremely old now, like 70 years old".
- **Who ages, and how much** (27 September). "Thaer isn't old because of his royal elf blood directly. Leorin is just related to royal blood. Her father just looks a little older." So direct royal blood barely ages in a thousand years, and Leorin, who is only related to it, has grown old.
- **Elowen** was Seralune's attendant before the seal.
- **Cyrandor** stays, with his name, as the keeper of the queen's Order. The old image of him weeping and dropping his linen changes: "something else better suited".
  - **To Nereth** (27 September): "He is her mentor, almost a father figure. He taught her everything in the castle, and how to work and do things."
- **No wardwrights, and no silver chain.** The author: "I don't like the silver chain and there are no wardwrights."
- **The king is away.** Natharul's scouts told him to come and see a battlefield with dead elves on it, thinking Mydea killed his people. (Chapter 1 already has "pale soldiers with pointed ears" among the dead.)
- **The palace and the city** are built together from the author's picture: "we can change this together". The picture so far (27 September):
  - **Natharul is both the continent and the kingdom.**
  - **The palace** is massive, on a hillside, "like a kingdom in FF16 and the elven kingdom of Rivendell in LOTR".
  - **The waterfall** beside it is huge, "bigger than a massive building". It's holy: it represents life to the elves, and they believe it supplies life to the lands of Natharul.
  - **A massive forest** lies below.
  - **The city** lies inside the forest, "like Oriflamme" (FFXVI).
  - **The royal battleship** flies. The king took it to Mydea, and no rider can catch it.
  - **The royal tree** stands at the top of the waterfall, and can be seen from the castle. It's just a tree, with no symbols. It's far bigger than it was a thousand years ago, so the sight of it shocks her, because to her it was a smaller tree yesterday.

## Brand (later-volume concept)

Not in the central cast yet, and not locked (handoff §7, §14.3).

- The same age as Alaric. The strongest living Fire user, whose fire can burn white. He fights with Natsu's exuberant physicality and energy (*Fairy Tail*).
- **First version (§7):** he sincerely believes he's a good person, because he was raised in a world that treats great power as moral authority.
- **Newer version, under discussion (§14.3):** he's being considered as the Ruler of Fire. The author wants some of Zenos's obsessive hunt (FFXIV), with more exuberance. He first thinks Alaric insignificant; curiosity becomes fascination, then obsession, as Alaric survives impossible things. He doesn't care much about Kelmend, the hierarchy or public heroism; he wants strength and a worthy opponent. The reader should find him infuriating, frightening and still charismatic: an "evil best friend" who decides Alaric is his rival without asking. He lasts several volumes.
- Which version holds, and whether he appears in Volume 1 at all, is open.

## The friends

- **Alaric's:** Silas, Redd and Wena stay, and a new character joins: Freya, Redd's younger sister. **Seralune's:** Nereth stays.
- **Each gets a full reset** of character, to make them unique.

### Silas

- He still loves Marta.
- **Gerolt's pupil.** He was Gerolt's underling and pupil, which is why he acts like him. But he's far more harsh.
- **Reference:** Guts (*Berserk*).
- **Method.** He just wants to get things done, even if it means violence. He is brutal in his ways and in his killings.
- **Affinity:** Fire, Eminent, the same level as Gerolt.
- He still teaches Alaric the sword.
- **What he takes from Guts:** pragmatism in brutality. He is very, very cunning.
- **The gorge survives.** His old squad and Marta's father were all killed. He lives with the guilt every day, blames himself, and lost the woman he loves most in the world: they were going to be married before it happened.
- **How he came to Avarice (my reading of "he was a part of it", to confirm):** he was once part of the system, then fell in love with Marta and the cause she fought for.
- **The difference from Gerolt:** Silas always wants to win, by any means necessary. Gerolt holds back; Silas doesn't.
- **Flaw:** he acts instead of thinking, though he's working on it.
- **Want:** to fix the past.
- **What he must learn:** to live with and accept his actions, and that the past can't be changed. He has to accept his flaws and grow as a man.
- **Underneath:** a loving, caring man who just wants to protect his comrades.
- **Cunning in the moment, reckless in the big choices** (like the gorge).
- **Gerolt taught him in Avarice.** Gerolt was angry that Silas didn't learn from his teachings.
- **He knows his master's blade on sight.** In the redesign he comes because he heard the fight, not for the sword. When he sees the sword across Alaric's lap his face changes (Chapter 2). In Chapter 3 he picks it up from the riverbank and gives it back, and doesn't let go of it straight away.
- **His consequential mistake in Volume 1** (handoff §15.7): he chooses brutality, and leaves an easy trail for pursuit.
- **He's at Gerolt's last stand** (27 September, Chapter 2). He cuts down the remaining riders, and he and Alaric run. **Where he lives** (27 September): "He lives on the river to stay away from people. He is near Kelmend because he loves Darcy and wants to keep up to date with any news related to her." The author then corrected "Darcy": "I meant Marta, sorry." So he loves Marta, and he lives on the river near Kelmend for news of her. Why he's there: "Silas is at the river, he 'stays' there. He heard the elves and the fight, so he came to see what it was, and sees his former master fighting to the death." Gerolt sees him, gives a small "heh", and never speaks again.

### Wena

- **She stays as she is:** Gerolt's large farm dog, and only ever an animal.
- **Gerolt's dying gift,** alongside the sword. It's almost a wish to keep her safe.
- **Who she attaches to:** Alaric, but often Freya more than anyone else.

### Nereth

- A servant maid. Fire.
- She still gets corrupted, and she lives through the entire series.
- **References:** Ram (*Re:Zero*) and Revy (*Black Lagoon*).
- **Character.** She grew up a servant and still acts like one. She is loyal to a fault, and doesn't like to slip.
- **What she wants for herself:** to explore the world. She has wanted to see the sights of the world since she was a child.
- **Being decided for.** She doesn't like it, but as a maid and servant she follows orders.
- **Ram on duty, Revy when she slips.**
- **Seralune's feelings make her corruption flare.**
- **Her first refusal of Seralune comes later,** not in Volume 1.
- **Always composed on duty** (27 September). Her first slip comes in the escape, not before.
- **Cyrandor's order** (27 September): "Secretly, before meeting Seralune, Cyrandor told Nereth to watch over Seralune: even if she seems dangerous, she is important. Nereth obeys, but is struggling to understand why her." This replaces the old canon that she has nothing to do with the Order.
- **Her first disobedience of anyone** is still undecided (handoff §15.10). Her first *slip*, from Ram to Revy, comes in the escape (above).

### Redd Vander

- **Family.** Freya's older brother. They share the same backstory.
- **Hatred.** He hates, hates, *hates* elves for what they did to his village and his family.
- He carries his father's sword. He still names Alaric "Al" later on.
- **Magic.** Low Earth; that's simply what he is. No hidden power.
- **Age:** 28.
- **After the village burned.** He was 8 and Freya was 1. They survived on the road for two years before coming to Kelmend.
- **Tested and put in service.** He was tested at ten, two years after the fire. Both children were taken, and he was put in service to someone in Kelmend. He takes care of his sister, because she had nowhere else to go.
- **His master died of old age.** He is no longer in service when Alaric meets him. He's unclaimed: nobody cared enough to reassign him.
- They grew up in Kelmend's Faint quarter.
- **Character.** Warm and funny, and carries pain. His humour is how he butts heads with Silas, and how he shows he cares deeply for his sister.
- **Lives in the present.**
- **Flaw:** he's often too carefree when seriousness is needed.
- **Reference:** Natsu (*Fairy Tail*).
- **How he differs from Silas:** Silas acts carelessly with violence; Redd acts carelessly out of joy.
- **What he is to the group** (handoff §15.8): emotional support and its connective tissue. He pushes people to become better. The irony is that the person holding the group together is full of hatred towards elves.

### Freya Vander (new)

- **Age.** 21: Redd's younger sister, one year older than Alaric.
- **Backstory.** The same as Redd's, but she was too young when it happened.
- **Magic.** Eminent Water, but she was never tested. She grew up with Redd in Kelmend's Faint quarter.
- **How she avoided testing.** Kelmend's guards held inspections every year. Redd always hid her until she was older.
- **She doesn't know she's Eminent,** but she can use her magic decently well.
- **Her Eminence isn't for anything** (27 September). The author: "Nothing, she just is, and maybe never even learns it."
- **She hates fighting** (27 September).
- **Elves.** She doesn't hate them.
- **Her brother.** She admires him greatly, follows him and clings to him, and leans on him too much.
- **What she wants** (handoff §15.9): for her brother to find peace. Though younger, she's emotionally mature. She leans on Redd while also trying to make him better, giving up her own happiness and feelings. She must learn that Redd is his own person, and become her own. *Still open: what she would want for herself if Redd were safe and Alaric had never come.*
- **What she must learn:** to be her own individual person.
- **Alaric.** She finds admiration in Alaric: someone who is nothing, wanting to learn who he was.
- **Romance (proposed by Claude, approved by the author).**
  - **Volume 1: he doesn't see it.** She falls for him, grounds him and starts leaning on him. He gets flustered, but his mind is on who he *was*. The reader sees the life he's missing. When he shuts everyone out at the end, she's one of the people he shuts out.
  - **Volume 2: he starts to see her,** as part of learning to accept help. Their arcs cross: he learns to lean on others while she learns to stand alone.
  - **Volume 3, or whenever it's earned: something real and mutual.** It happens only once she's standing on her own, so it's love, not dependence. It's built from shared life, never from fate.
  - **When Seralune enters his life,** his feelings for her must grow from what happens between them in the present, starting with real friction. The soul bond never decides.
  - **How it ends: Freya chooses.** She sees where his life is going and chooses a life that's hers. She stays his friend, and is among the friends whose free future is the point of the series ending.
  - **Guardrails.** He never treats her as a placeholder. She never leaves the story through tragedy. Readers will split, and that's accepted.
- **Her arc.** Her dependence traps her: she starts leaning on Alaric the way she leaned on Redd. She climbs out of it by learning to love herself, and him.
- **The handoff on their love** (§18) discusses it volume by volume, with the risks to avoid. Its scenes and timing are proposals, and the questions it leaves open are in its §18.12.
- **Reference:** Tifa (FFVII): her warmth, and the way she grounds someone.

## World

### The erasure

- **No one in the world knows Alaric from the past.**
- **Except Time.** The Time bearer of a thousand years ago knew Alaric, and wanted to protect him against the coming war. That bearer's memories passed through time, because *time* remembers, not the person. The current Time bearer (in Kozmagar) doesn't know why he says "He's back." It just comes out.
- **The ancient Time bearer took part in the ritual,** but activated a part of the spell that sent Alaric into the future instead, to protect his dearest friend: Alaric.
- **The distance was random.** He just activated his Time magic; he didn't choose a thousand years. It could have been any length of time.
- **Deliberate parallel:** both protagonists were saved without their consent by someone who loved them. Thaeroval sealed Seralune; the Time bearer sent Alaric away.
- **Seralune does not remember Alaric** at the end of Volume 1.
- **A thousand years, rounded** (27 September). "It isn't exactly 1000 years; it's random, but rounded to 1000 years."

### Seralune's mother, the queen

- She opposed the sealing because she believed Seralune's mana could be controlled.
- She ran away because everyone else agreed to seal her daughter. She was distraught, but always believed her daughter would wake again.
- She set trustworthy servants to report back to her. When that generation aged out, the duty was passed down by word through the Order.

### Magic and Affinity

- "Magic" is the ancient word for Affinity. It was the word before the laws came in and the current world adopted the current meanings.
- **The class system still stands as in the old World Bible** (confirmed for Chapter 1, revision 1): Exalted, Eminent, Common and Faint. Every child is tested at ten, and children who test Faint are taken from their families under what's called protection.
- **Magic costs its user when cast on themselves.** A Fire user isn't immune to fire: if Gerolt casts fire on himself, he gets burnt. (The existing Chapter 1 candle line already obeys this: "The flame burned him. He did not pull away.")
- **Mana and Affinity** (handoff §3, from Chapter 4). Mana is the fuel; an Affinity is the force or element that gives it shape.

### The Eight Rulers (author-set, handoff §14.4)

- **Eight singular Ruler domains:** Light, Dark, Spirit, Time, Fire, Water, Wind and Earth.
- **The working grouping:** the Veiled Four (Light, Dark, Spirit, Time) and the Elemental Four (Fire, Water, Wind, Earth).
- **At most one living Ruler** holds each domain at a time.
- **A Ruler is born carrying the mantle.** It isn't achieved through training.
- **No successor can be born while the current Ruler lives.** Any irreversible death triggers succession: age, disease and accident count, and murder isn't needed.
- **After a death the mantle passes to a newborn.** It may choose the first suitable child, or stay unheld for years before it settles. The signs in an infant are subtle, and who the child is may only be found out later. The mantle goes to a child, never to the killer.
- **The Veiled Four are really different in the cosmology** from the Elemental Four. Religion may rank the Veiled Four "above", but that gives them no automatic advantage in a fight.
- *Known and proposed bearers:* Light, Atera (Mydea); Dark, Thaeroval (Natharul); Spirit, Natharul's formal Hero; Time, a beastfolk bearer in Kozmagar; Fire, Brand is being considered. Water, Wind and Earth aren't designed. Kurdag stays an Exalted Earth user, not automatically the Ruler of Earth. Ordinary Fire, Water, Wind and Earth users go on existing beneath their Rulers.
- *This supersedes the handoff's earlier idea of "Full Elemental users" (§7).* The handoff's interpretations (§14.4: vacancies, states hunting infant Rulers, the age-ten test as a search for missing Rulers, "Ruler" as a human title) are proposals.

### God and the fading world (author-set, handoff §14.5)

- **God is dead, or may never have existed.** The quotation stays central, but no moral deity needs to exist in the cosmology.
- **The world itself is becoming unstable and weak, and is slowly fading.**
- **The world put an extraordinary amount of its remaining energy into an attempt to correct that decline.**
- **Alaric and Seralune are the result of that attempt,** and a flaw in its ordinary order.
- *The handoff's working model (§14.5: circulating mana, the Eight mantles and a deep restorative reserve; one corrective soul anchored in two newborns, Alaric receiving the structure and Seralune the power) is unapproved in its details.*

### One soul, two people (author-set, handoff §14.5, §14.7)

- **Alaric and Seralune were born at exactly the same moment.**
- **They share the same soul, but are not the same person.**
- **If one of them truly dies,** the other doesn't die straight away, but becomes profoundly destabilised, as though reality no longer knows how to hold them.
- *Unresolved (handoff §14.1, §14.6):* the older statement that all four Veiled Affinities are dormant inside Alaric. The handoff's proposed replacement (Alaric has root-level channels into the Veiled laws, and Seralune's mana running through him pulls on the one existing mantle, so the living Ruler feels it leave) isn't approved.

### The ancient relationship (author direction, handoff §15.3–15.5)

- **The promise was private,** between Alaric and Seralune, not publicly known.
- **Their ancient failure was mutual.** Each believed they could save everyone alone and decide what was best for other people, and that helped turn the world against them.
- **They were married, or about to marry.** They loved each other deeply. When they saw destruction spreading around them, they fled together, and the hunt for them widened into war. *Which one (married, or about to marry) is not chosen.*
- **The ancient promises don't bind the present people.** Present Alaric and Seralune are meaningfully different people from their ancient selves, and neither owes the other romance because of a past relationship.

### The Silent Field

- **No one on the battlefield was on his side.** Every army there was fighting him and Seralune.
- **The riders (Chapter 2's Natharul scouts)** come because they've seen dead elves. They're shocked they neither saw nor heard the battle, and they want answers from the farmer whose land it is.

### Geography

- **Kozmagar is a separate continent,** the beast continent.
- **Natharul is both a continent and the kingdom on it** (27 September). See "Natharul's palace".
- **Gerolt's nearest neighbours** live two fields over, in a house with children. They're unnamed, and nothing else about them is decided.

### Ranks

- "High" was a mistake; the rank is **Eminent**. Liluth is Eminent Earth.

### Mydea

- A kingdom ruled with an iron fist. It wants to know everything, everywhere.
- Gerolt would be punished for hiding things.
- People talk, and aren't afraid to give each other up for extra food and gold.
- **Who rules:** the church gives the big orders. The king is a puppet who watches and enjoys his wealth. He's a vile dictator who only wants things for himself, and is introduced in Volume 2.
- **How the king is evil (Option A, chosen):** he chose his strings. He handed the church the kingdom, and bowed to Natharul, to keep his throne and his comfort. Every law carries his seal; he could stop any of it and never does. His existing footprint in Volume 1:
  - "The king's got the palace." (Chapter 25)
  - "The king bowed first. In his own hall." (Chapters 26, 27 and 30)
- **Natharul's scouts:** under the agreement between Mydea's king and Natharul, Natharul scouts are all over Mydea, all the time, scouting everywhere. They are never seen. That's the rule, to keep people calm.

### Avarice (formerly the Broken Shield network)

- The network survives under the new name.
- They fight. Everyone calls them Avarice because they're "evil" for trying to destroy the institution.
- **What they fight:** the whole church, and the Affinity laws.

## Open questions

### Volume 1 picture

- **Does Seralune believe it was her fault?**
- **When does the truth come out, and to whom?** Which volume?
- **Seralune and the question:** does her Volume 1 answer the same question from the other side? She has infinite mana, yet is treated as defective and dangerous.
- **Seralune's external goal** in Volume 1.
- Beyond the dead and his guilt, what else can never go back to how it was?

### Volume 2 picture


### Freya and Seralune

- **Do Freya and Seralune have a relationship of their own?** Freya doesn't hate elves. In FFVII, much of why readers love the Tifa and Aerith triangle rather than resent it is that the two women respect each other.

### Chapter 1

- Should Chapter 1 hint at his willingness to kill? "Chapter 1 is about him not knowing anything" suggests not. *Confirm.*
- Should Chapter 1 carry the horror that nobody on earth knows him? It's the opposite of Subaru's situation, where everyone knows him and he doesn't know them.

### Seralune

- **What does "tsundere" look like for her?** The design bible warns against "flirtation wearing armour", so her friction with Alaric needs a real source. One candidate from existing decisions: she can't stop helping and takes control to do it, while he won't let anyone help him.
- **"The best image": in whose eyes?** The court's, the people's, Nereth's?
- **One question, two verdicts (my reading, to confirm).** The world tells him he's nothing and tells her she's dangerous. By the end of Volume 1 each believes the verdict: he is nothing, she is the problem.
- **Shoko's darkness.** In the film, Shoko's self-blame leads her to a suicide attempt. Is that depth part of what you're taking, or only her gentleness and her apologies?
- **Her mother's opposition.** Does Seralune learn it from the Order, as she did from Cyrandor in the old version?
- **The trail.** How far does her mother's trail get in Volume 1? In the old version it ended in ashes at the Lily Steps.

- **Two internal wars at one climax.** His ("Why me, when I'm empty?") and hers ("Why must I? But I should.") need different shapes. She keeps her own sensory language and doesn't borrow his.

### Time

- **Did anyone in the ancient coalition learn what he did,** and what happened to him?
- **Does Time remember inside Alaric?** He carries Time too, dormant.

### Silas

- **Is Silas a mirror of Alaric?** Alaric chases a past he can't remember; Silas can't stop reliving one he knows too well. Both must learn to live now.

### Redd and Freya

- **Does the reader ever find out Freya is Eminent, and through whose eyes?** She may never learn it herself (27 September). If the reader is told, they'll wait for it to matter. If the state learns it, it will want her, as it wanted Marta.

### Nereth

- **Her speech as a gauge.** Could the way her speech slips mark both closeness and anger? *(Proposed by Claude.)*
- **Her dream, fulfilled the wrong way.** She finally sees the world, but as a fugitive servant with a spreading corruption, and ends Volume 1 held by the Holy bearer. Should Volume 1 still give her real moments of wonder?

### Veiled Affinities

- **Is it a general rule?** When Alaric uses a Veiled Affinity, does its living bearer always feel it pulled out of them for a moment? If so, it answers an old open question: his Affinities aren't duplicates of the bearers', they're the same thing. It also means Thaeroval would feel Dark, Atera would feel Light, and the Time bearer would feel Time.
- **Which bearers felt the tear?** The tear in Volume 1 passed Seralune's power through his Affinities. Under this rule, which bearers felt something pulled at that moment? In the old Chapter 30, Atera was destroyed and rebuilt on the stair.
- **When do readers learn the souls went to the Last Dark?** Alaric can't know it, so the narration can't say it in Volume 3. It could be a later reveal that makes Volume 3 painful to reread.
- **The Last Dark and the ending.** Does anything ever come back for the souls he cast out? *(The ending no longer rests on a Soul World reunion; see The series. If the Soul World survives the end of magic, it must be something other than mana: handoff §14.10.)*

### Gerolt

- In a state that uses people by rank, how did an Eminent get to retire?
- What is the name he swallows when the riders arrive in Chapter 1? It's more specific than "Natharul", which he has already said aloud.
- Where does his damage come from?

### World

- Does anyone in the present day still say "magic"? Redd says "I *dislike* magic" in Chapter 20.
- Who changed the word from Magic to Affinity, and when?
- **The king's appetite:** what does he spend his comfort on? Two options were offered alongside A and not chosen:
  - **B. The watcher.** The informers' reports end on his desk, and he uses them for private appetites.
  - **C. The collector.** His wealth includes people.
- **The scout agreement.** Who knows it exists? Is it an open secret, or known only to the court, the church and people like Gerolt? Does Gerolt know it from his past?
- **How do the scouts stay unseen?** Magic, skill, or both? The Chapter 1 dismount that makes no sound may already be showing how.
- **The church's reach:** how does the church reach a farm like Gerolt's? A shrine, a priest with a ledger, informers?
- **The field:** who suppresses the Silent Field in Chapter 13, the church or the army?

### Avarice

- Does Avarice fight the faith itself, or only the church as an institution? How does it treat sincere believers, such as Idony, Aubin and the pilgrims?
- What do its members call themselves? Does the split-shield symbol survive?
- Is there a problem with Re:Zero readers linking "Avarice" to Re:Zero's Greed (its Witch and Archbishop of Greed)?

### From the handoff (29 September)

Each of these is open. The handoff's recommendation, where it has one, is in the section named.

- **Chapter 5.** Seralune's first active choice (§15.2), the dramatic question of each part (§14.2), and Nereth's first disobedience (§15.10).
- **The Volume 1 structure.** The proposed 50–54 chapters in nine movements (§19). Its full working file, `Volume 1 Structural Map - Proposal.md`, isn't in this repository.
- **The core's answer.** What Alaric actually gets from it, and in how many stages (§14.2, §19.5 proposes three: the Silent Field, Foramen, Favale).
- **Foramen.** Does Kurdag hide the cost of living there, or do its people choose the risk knowing it (§14.2)? Does it expel Alaric, or does he leave by choice (§14.2, §19.4)?
- **Inrandeel.** Who destroyed or removed the independent elves, and what concrete clue sends Seralune on to Favale (§14.2)?
- **The child at the tear.** Only if the child has a family, a life and a reason to be in Favale first (§14.2, §16.8).
- **Silas's trail.** Does it lead Liluth, Brand or both to Foramen (§15.7)?
- **Redd.** What only he can do, and what he wants for himself (§15.8).
- **Freya.** What she would choose for herself (§15.9). The open questions about her and Alaric (§18.12).
- **The ancient past.** Married, or about to marry (§15.4)? What exactly did they attempt that went wrong, and who could refuse it (§15.3)? What span of memory did the ritual take from Seralune, if her "yesterday" was years before the final battle (§15.5)?
- **The cosmology.** What is causing the world's decline (§14.10)? Is Seralune's mana truly endless, or only endless as far as anyone can measure (§14.5)? How does Alaric relate to the four Veiled mantles (§14.6)? What happens to the survivor if one of them dies (§14.7)?
- **The Rulers.** Who holds Water, Wind and Earth, who the Time and Spirit bearers are, each Ruler's limits, whether they age normally, and what counts as true death for Atera (§14.4).
- **Brand.** Which version, and when he first appears (§14.3).
- **The ending's mechanics.** How the unbinding works and what each person gives up (§17).

### Reference material

- Re:Zero Arc 6, Chapter 57 onward couldn't be read. This environment's network policy blocks witchculttranslation.com. Either allow the domain in the environment's network settings, or paste the text.

## Existing files that now conflict

None of these have been changed yet. They're listed so nothing is forgotten when we reach those chapters.

### "High" becomes Eminent

- `Old - Before Re-plan/World Bible/The World.md:874`: the Wind rider is "High".
- `Old - Before Re-plan/Chapter Design/Chapter 7 - Story Design.md:259`: Marta is "a High Wind user". The World Bible already says Eminent.
- `Old - Before Re-plan/Chapter Design/Chapter 20 - Story Design.md`, lines 84, 85, 291 and 652.
- `Old - Before Re-plan/Chapter Design/Chapter 6 - Story Design.md:54`: "not High".

### Silas arrives in Chapter 2

- In the old version Alaric is alone from Gerolt's death until he meets Silas at the river (old Chapters 3–6). Now Silas is with him from the end of Chapter 2, so old Chapters 3–6 change: the escape, the river crossing, and Silas recognising the sword.

### The token becomes the sword

- Gerolt's split-shield token appears in Chapters 2, 3, 6, 7 (14 mentions), 8, 12, 13, 14 and 15. The sun tokens in Chapters 24–30 are unrelated.
- The token currently does three jobs, and each needs a new carrier:
  - Marta's trust (Chapter 7);
  - Silas's decision to help (Chapter 6): **resolved.** He recognises his master's sword;
  - proof of the network connection.
- The sword also changes:
  - Gerolt's death in Chapter 2, which currently happens with the sword raised;
  - the escape through the wheat and across the flooded river (Chapters 3 and 6);
  - Silas giving Alaric a spare sword (Chapter 18);
  - Liluth recognising the sword (Chapter 20 design).
- Chapter 3's cabin explosion ("something hit the cabin. The night went orange") is never attributed. It could become Gerolt's last stand without rewriting that scene.

### Silas is now Eminent

- The old Silas was upper-Common Fire. See the Silas entry in `Old - Before Re-plan/World Bible/The World.md` and `Old - Before Re-plan/Chapter Design/Chapter 6 - Story Design.md:54` ("upper-Common Fire『Affinity』, not High").

### Redd loses his hidden power; Freya is new

- The old Redd has hidden Exalted Earth: the title of his entry in `Old - Before Re-plan/World Bible/The World.md` (line 876), and `Main Characters.md:362`. Scenes that relied on big, wild workings need rethinking for low Earth. Examples: the earth shelf that holds up Foramen's wall (Chapter 20), and the heaved flagstones in Helmi's house (Chapter 26).
- The old Redd was never tested and "No master owns him" (`The World.md`, Redd entry). Now he was tested at ten and served a master in Kelmend until the master died of old age.
- The old Redd has no sister, so every scene with Redd changes.

### Broken Shield becomes Avarice

- `Old - Before Re-plan/World Bible/The World.md` (8 mentions).
- Chapters 2, 6, 7 and 8 in `Old - Before Re-plan/Volume 1 - Rewrites/`.
- The Chapter 3, 6 and 7 designs.

### Magic and Affinity

- `Old - Before Re-plan/Volume 1 - Rewrites/Chapter 6 - The Road Owed to the Dead (Rewrite).md:419`: "Fire『Affinity』" surfaces "with the same unwanted certainty as『Magic』". Under the new rule, "Affinity" is Gerolt's modern word, not buried knowledge.
- `Old - Before Re-plan/Volume 1 - Rewrites/Chapter 20 - Liluth (Rewrite).md:249`: Redd says "magic". This depends on the open question above.
- `Old - Before Re-plan/Volume 1 - Rewrites/Chapter 2 - The Price of a Voice (Rewrite).md`: "Not some quiet idea you talked about over stew" changes if the flame scene goes in.

### Natharul scouts: always present, never seen

- `New - Re-plan/Volume 1/Chapter 1 - A War Without Sound.md:621`: "Riding openly across Mydean fields… They shouldn't be here. Not ever." Under the new rule the scouts are always here. What should shock Gerolt is that they can be *seen*: they're riding openly with torches. *Revision 1: now "They're letting themselves be seen" (change 36). The line number refers to the draft in `Volume 1/Drafts/`.*
- `Old - Before Re-plan/World Bible/The World.md:359` says the same thing and treats it as a breach of the peace arrangement.

### No one knows Alaric from the past

- `Old - Before Re-plan/World Bible/The World.md:1049`: the old epilogue's "He's back" is resolved (Time remembers, not the person), but the old ritual design in `The World.md` ("The Erasure Ritual") says Alaric's own Affinities resisted the spell and the Time component displaced him by accident. Now the displacement is the ancient Time bearer's deliberate act. Does his own resistance still play a part?

### The seal, the wardwrights and Nereth (Chapter 4, round 1)

- `Old - Before Re-plan/World Bible/The World.md`, "The Queen's Order", says Nereth "is **not** secretly a member". Now Cyrandor has told her to watch over Seralune.
- The old Chapters 3–5 and their designs: the carved circle and its metal strips become the crystal, and the wardwrights and the silver chain are gone.
- `Old - Before Re-plan/World Bible/The World.md`, "Elven aging": royal bloodlines age "at a vastly slower rate", so a thousand years barely shows. *Settled in Chapter 4, round 2:* that holds for direct royal blood; Leorin, who is only related to it, looks about seventy.
- The old Chapter 4: the royal tree carved with nine stars where there were four. The tree is now a real tree at the top of the waterfall, with no symbols, grown far bigger.
- The old Chapters 3–4: Seralune tries to make light, and her mana flares the lamps. Under the new rule her mana can't be used at all, and it never flares.

### Thaeroval feels nothing

- `Old - Before Re-plan/World Bible/The World.md:1049`: the old epilogue has Thaeroval's sword "won't stop humming". Check it against "he feels literally nothing" when the epilogue is replanned.

### Seralune's opening chapters (added 29 September)

- The old Chapters 4 and 5 (`Old - Before Re-plan/Volume 1 - Rewrites/`) are replaced by the new Chapter 4, the agreed Chapter 5, and the escape in Chapter 7. Chapter 4's design settled most of the old material (Leorin, no wardwrights, nobody saying "sealed" or "a thousand years"). What's left undecided is the old escape: Cyrandor losing an arm, Nereth's rescue, Thaer at the stair and the drainage channels.
- `Old - Before Re-plan/World Bible/The World.md` has Thaeroval hating Alaric and designing or completing the erasure ritual. The handoff now has him regretting the sealing and delaying the reseal. Whether the old history still stands behind the new regret is open.
- The old route took Seralune by ship from Waluna to Meren, then to Favale. The new direction sends her into Mydea, possibly by way of Inrandeel.

### Chapter 1 fixes from the first review

Revision 1 (see `Volume 1/Chapter 1 - Changes.md`) deals with the ones inside Chapter 1. The callbacks in old chapters wait until those chapters are replanned.

- "Empty" is never spoken, but Chapter 2:305 and Chapter 7:567 and :601 depend on it. *Revision 1: now spoken (change 25).*
- Gerolt's mug gesture is recalled in Chapter 13:333.
- Gerolt's beastfolk line is quoted in Chapter 28 (Part 2):39. *Revision 1 leaves that line as it was.*
- Time of day: "senseless since morning" clashes with noon and Chapter 2's "this afternoon". *Revision 1: now "since midday" (change 11).*
- Line 235 has a point-of-view slip: he "talked through the whole walk back" while the boy is unconscious. *Revision 1: fixed (change 8).*
- Line 137 repeats "no wound" from the opening. *Revision 1: fixed (change 7).*
