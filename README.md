# The Ruler of Nothing

A long-form fantasy web novel, planned for at least twelve volumes.

Alaric wakes on a battlefield nobody heard, with no memory and no 『Affinity』. He's in a world that ranks every person by their magic and takes the children who test weakest. At the same instant, Seralune, a princess of Natharul, wakes alone inside a broken crystal seal, a thousand years after the last day she remembers.

> **What is your worth when everyone tells you that you're nothing?**

The story is being re-planned and rewritten from the beginning, one chapter at a time, starting in September 2026. Volume 1 is in progress.

## Read the novel

**Volume 1:** ten chapters finished, about 45,800 words. Chapter 11 is next.

| Ch | Title | Viewpoint | Words |
|---:|---|---|---:|
| 1 | [A War Without Sound](Manuscript/Volume%201/Chapter%2001%20-%20A%20War%20Without%20Sound.md) | Alaric | 6,122 |
| 2 | [The Price of a Voice](Manuscript/Volume%201/Chapter%2002%20-%20The%20Price%20of%20a%20Voice.md) | Alaric | 4,639 |
| 3 | [The Weight of the Living](Manuscript/Volume%201/Chapter%2003%20-%20The%20Weight%20of%20the%20Living.md) | Alaric | 2,056 |
| 4 | [A Promise Left Fractured](Manuscript/Volume%201/Chapter%2004%20-%20A%20Promise%20Left%20Fractured.md) | Seralune | 2,585 |
| 5 | [The Shape of Absence](Manuscript/Volume%201/Chapter%2005%20-%20The%20Shape%20of%20Absence.md) | Seralune | 3,138 |
| 6 | [The Words of the Dead](Manuscript/Volume%201/Chapter%2006%20-%20The%20Words%20of%20the%20Dead.md) | Alaric | 4,868 |
| 7 | [The Last Keeper](Manuscript/Volume%201/Chapter%2007%20-%20The%20Last%20Keeper.md) | Seralune | 4,220 |
| 8 | [The Road Owed to the Dead](Manuscript/Volume%201/Chapter%2008%20-%20The%20Road%20Owed%20to%20the%20Dead.md) | Alaric | 5,312 |
| 9 | [Refuge](Manuscript/Volume%201/Chapter%2009%20-%20Refuge.md) | Alaric | 4,132 |
| 10 | [Beneath Natharul](Manuscript/Volume%201/Chapter%2010%20-%20Beneath%20Natharul.md) | Seralune | 8,698 |

## How the repository is organised

```
Manuscript/                      Finished chapters, and nothing else
  Volume 1/

Story Bible/                     What is true in the story, and what is planned
  Decisions.md                   Every decision, and every open question
  Volume 1 Picture.md            The shape of Volume 1 on one page
  Volume 1 Outline (Chapters 5-15).md
  Volume 2 Picture.md
  Volume 3 Picture.md
  Handoffs/                      The author's handoffs, kept word for word
  Proposals/                     Ideas under discussion, not canon
  Craft/                         The narrative and web-novel design bible

Chapter Development/             How each chapter was made
  Volume 1/
    Chapter 01/ ... Chapter 11/  Designs, dialogue rounds and changes
      Drafts/                    Saved drafts and change lists

Archive/                         Everything written before the re-plan

.claude/skills/chapter-rewrite/  The rewriting method and its two tools
```

### Where to start

- **To read the story:** `Manuscript/`, in chapter order.
- **To check what's canon:** [`Story Bible/Decisions.md`](Story%20Bible/Decisions.md). It overrides every other file. The [Volume 1 Picture](Story%20Bible/Volume%201%20Picture.md) summarises it on one page.
- **To see how a chapter was made:** open its folder in `Chapter Development/`. Start with the design, then the dialogue rounds, then the changes.

## Story Bible

| File | What it holds |
|---|---|
| [Decisions.md](Story%20Bible/Decisions.md) | Every decision made with the author, in the author's words where possible. It has a section per chapter, character and place, then the open questions and the old files that now conflict. |
| [Volume 1 Picture.md](Story%20Bible/Volume%201%20Picture.md) | Volume 1's question, arcs, cast, road, ending and the story so far. |
| [Volume 1 Outline (Chapters 5-15).md](Story%20Bible/Volume%201%20Outline%20%28Chapters%205-15%29.md) | A rough plan of Chapters 5 to 15. Each chapter is designed in detail only when it's next. |
| Volume 2 Picture.md, Volume 3 Picture.md | The early shape of the next two volumes. |
| `Handoffs/` | The author's handoffs from work outside this repository (29 September, 1 October, and Marta's voice on 2 October), and Claude's reply to the first one. |
| `Proposals/` | The 50–54-chapter structural map for Volume 1, and ten explanations for the dying world. Both are for discussion; neither is approved. |
| `Craft/` | The craft reference: page style, character voices, scene and chapter design, and web-serial rhythm. |

## Chapter Development

Each chapter has its own folder. Its files are named after the chapter, so they stay easy to find in search.

| File | What it is |
|---|---|
| `Chapter NN - Design.md` | The plan, agreed with the author question by question before any writing. |
| `Chapter NN - Dialogue...` | The key exchanges, in the author's rough words, then in each character's voice. |
| `Chapter NN - Changes...md` | Every change made to the chapter, with its before, after and reason, round by round. |
| `Chapter NN - From the Old Chapters.md` | The new chapter compared with the pre-re-plan material it replaces. |
| `Drafts/` | Saved copies of the chapter at each stage, which are never edited, and the change lists that produce the changes files. |

Files marked "kept word for word" (the author's pasted designs, dialogue, handoffs and other workspaces' drafts) keep their original text. A few of them name files by the paths they had before the reorganisation of 6 October 2026.

## How the work is done

- **One chapter at a time.** The design is agreed first, with questions asked a few at a time. Then comes a round of dialogue options for the important exchanges. A chapter is written only after the author's go-ahead.
- **Decisions are recorded as they're made.** Every answer goes into `Decisions.md` before it goes onto the page.
- **Every revision is a change list.** Changes are never made to a chapter by hand. Each one is written as an entry in the chapter's change list, and a script applies them to the saved draft. So the record of changes always matches the chapter exactly.
- **The rules of the method,** learned from the author chapter by chapter, are in [`.claude/skills/chapter-rewrite/SKILL.md`](.claude/skills/chapter-rewrite/SKILL.md). That covers where canon lives, how to work with the author, the writing principles, the house style and the final check. The folder name starts with a dot, so some file browsers and Obsidian hide it.

### Tools

Both scripts are run from the repository root.

```bash
# Apply a change list: writes the chapter and its changes file
python3 .claude/skills/chapter-rewrite/scripts/apply_changes.py "Chapter Development/Volume 1/Chapter NN/Drafts/Chapter NN - change list.json"

# Check that the chapter and changes file on disk match the list, without writing anything
python3 .claude/skills/chapter-rewrite/scripts/apply_changes.py "<change list>.json" --check

# Mechanical style check of a chapter
python3 .claude/skills/chapter-rewrite/scripts/style_check.py "Manuscript/Volume 1/Chapter NN - Title.md"
```

### House style

- **Spelling and punctuation.** British spelling, straight quotes, an em dash with no spaces, and the single "…" character.
- **Thoughts.** Italics for a character's immediate thought and for precise stress.
- **Corner brackets** for 『Affinity』, 『Magic』 and the rank 『Faint』.
- **Bold** only for **THOOM**, Alaric's heartbeat.
- **Point of view.** Close third person, one pair of eyes per chapter.

## Archive

Everything from before the re-plan is kept unchanged as raw material. It isn't canon: where it disagrees with `Decisions.md`, the decision wins, and the conflicts are listed at the end of that file.

| Folder | Contents |
|---|---|
| `Volume 1 - The Silent Field/` | The original drafts of Chapters 1–22, and the Arc 1 story basis. |
| `Volume 1 - Rewrites/` | The rewrite pass of Chapters 1–30 and Interludes I–IV. |
| `Volume 1 - GPT Rewrites/` | Two alternative rewrites of Chapter 1. |
| `Chapter Design/` | Chapter designs for Chapters 2–30 and Interlude IV. |
| `World Bible/` | Lore, characters, craft rules and story questions as they stood before the re-plan. |
| `Claude Outputs/` | Earlier copies of the rewrites, and dated backups. |
| `Chapter 1 Workshop/` | Chapter 1 drafts and helper scripts from the rewrite workshop. |
