#!/usr/bin/env python3
"""Apply a chapter's change list, then write the revised chapter and its changes file.

Usage:
    python3 apply_changes.py "<change list>.json"            # write both files
    python3 apply_changes.py "<change list>.json" --check    # write nothing; report if the files on disk are current

The change list names three files, each relative to the change list's own folder:
    "draft"         the chapter before revision (a saved copy that is never edited)
    "chapter"       the chapter to write
    "changes_file"  the before/after file to write

Every change replaces a run of whole paragraphs from the draft, so the changes file
always matches the chapter exactly. A paragraph is one line; paragraphs are separated
by one blank line (the house format). See SKILL.md for the change-list format.
"""
import json
import re
import statistics
import sys
from pathlib import Path


def paras(text):
    return text.split('\n\n') if text else []


def find_all(lst, block):
    return [i for i in range(len(lst) - len(block) + 1) if lst[i:i + len(block)] == block]


def line(i):
    return 2 * i + 1


def span(i, n):
    return (line(i), line(i + n - 1))


def lines(word, t):
    return f'{word} line {t[0]}' if t[0] == t[1] else f'{word} lines {t[0]}–{t[1]}'


def quote(s):
    return '\n>\n'.join('> ' + p for p in paras(s))


def stats(ps):
    body = [p for p in ps if not p.startswith('# ') and p != '---']
    wc = [len(p.split()) for p in body]
    text = '\n'.join(body)
    return dict(words=sum(wc), median=statistics.median(wc),
                nothing=len(re.findall(r'\bnothing\b', text, re.I)))


def fail(msg):
    sys.exit('apply_changes: ' + msg)


def main():
    args = [a for a in sys.argv[1:] if a != '--check']
    check = '--check' in sys.argv[1:]
    if len(args) != 1:
        sys.exit(__doc__)
    spec_path = Path(args[0]).resolve()
    spec = json.loads(spec_path.read_text(encoding='utf-8'))
    base = spec_path.parent
    draft_path, chapter_path, out_path = (base / spec[k] for k in ('draft', 'chapter', 'changes_file'))

    O = draft_path.read_text(encoding='utf-8').rstrip('\n').split('\n\n')
    for i, p in enumerate(O):
        if '\n' in p:
            fail(f'draft line {line(i)}: a paragraph runs over more than one line. Use one line per paragraph.')

    changes = spec['changes']
    cur = list(O)
    for n, c in enumerate(changes, 1):
        c['n'] = n
        label = f'change {n} ("{c["title"]}")'
        b, a = paras(c['before']), paras(c.get('after', ''))
        if c['kind'] not in ('changed', 'cut', 'added'):
            fail(f'{label}: kind must be "changed", "cut" or "added".')
        if (c['kind'] == 'cut') != (not a):
            fail(f'{label}: a cut has no "after"; every other kind needs one.')
        hits = find_all(O, b)
        if len(hits) != 1:
            fail(f'{label}: its "before" text appears {len(hits)} times in the draft. It must appear exactly once. '
                 'Copy it exactly, or include a neighbouring paragraph. To adjust an earlier change, '
                 'edit that change instead of adding a new one on top of it.')
        c['draft'] = span(hits[0], len(b))
        if c.get('decision') == 'rejected':
            continue
        hits = find_all(cur, b)
        if len(hits) != 1:
            fail(f'{label}: an earlier change already altered its "before" text. Merge the two changes.')
        i = hits[0]
        cur[i:i + len(b)] = b + a if c['kind'] == 'added' else a

    for c in changes:
        shown = paras(c['before']) if c.get('decision') == 'rejected' else paras(c.get('after', ''))
        if not shown:
            c['rev'] = None
            continue
        hits = find_all(cur, shown)
        if len(hits) != 1:
            fail(f'change {c["n"]}: its text is not in the finished chapter exactly once. Merge overlapping changes.')
        c['rev'] = span(hits[0], len(shown))

    def ref(tag):
        return ', '.join(str(c['n']) for c in changes if tag in c.get('tags', []))

    def fill(md):
        return re.sub(r'\{tag:([\w-]+)\}', lambda m: ref(m.group(1)), md)

    live = [c for c in changes if c.get('decision') != 'rejected']
    rejected = [c for c in changes if c.get('decision') == 'rejected']
    kinds = {k: sum(1 for c in live if c['kind'] == k) for k in ('changed', 'cut', 'added')}
    S0, S1 = stats(O), stats(cur)

    out = []
    w = out.append
    w(f'# {spec["title"]}')
    w('')
    w(fill(spec.get('intro_md', '')).rstrip('\n'))
    w('')
    w('## At a glance')
    w('')
    w(f'- **{len(changes)} changes proposed.** {len(rejected)} rejected so far, so {len(live)} are in the chapter: '
      f'{kinds["changed"]} rewritten, {kinds["cut"]} cut and {kinds["added"]} added.')
    w(f'- **Length:** {S0["words"]:,} words before, {S1["words"]:,} after.')
    w(f'- **Median paragraph:** {S0["median"]:g} words before, {S1["median"]:g} after. The house target is roughly 14–22.')
    w(f'- **"Nothing":** {S0["nothing"]} times before, {S1["nothing"]} after.')
    for g in spec.get('glance', []):
        w('- ' + fill(g))
    w('')
    w('## Your call')
    w('')
    w("Each of these needs a yes or no from you. It adds something about a character or the world "
      "that you haven't decided, or it's a change you didn't ask for.")
    w('')
    pending = [c for c in changes if c.get('call') and not c.get('decision')]
    for c in pending:
        w(f'- **Change {c["n"]}, {c["title"]}.** {c["call"]}')
    if not pending:
        w('- Nothing is waiting on you. Every change that needed your answer has one.')
    decided = [c for c in changes if c.get('decision')]
    if decided:
        w('')
        w('**Already decided**')
        w('')
        for c in decided:
            w(f'- **Change {c["n"]}, {c["title"]}:** {c.get("decision_short", c["decision_note"])}')
    if spec.get('summary_md'):
        w('')
        w(fill(spec['summary_md']).rstrip('\n'))
    w('')
    w('## The changes')

    headings = spec.get('sections', {})
    last = None
    for c in changes:
        if c['section'] != last:
            last = c['section']
            w('')
            w(f'### {headings.get(last, last)}')
        w('')
        w(f'#### {c["n"]}. {c["title"]}')
        w('')
        if c.get('decision') == 'rejected':
            w(f'*{lines("Draft", c["draft"])} · proposed, rejected by you: the original stays at {lines("revised", c["rev"])}*')
            w('')
            w('**Before (kept)**')
            w('')
            w(quote(c['before']))
            w('')
            w('**Proposed (not used)**')
            w('')
            w(quote(c['after']))
        elif c['kind'] == 'added':
            w(f'*Added after {lines("draft", c["draft"])} · now {lines("revised", c["rev"])}*')
            w('')
            w('**After this line**')
            w('')
            w(quote(c['before']))
            w('')
            w('**New**')
            w('')
            w(quote(c['after']))
        elif c['kind'] == 'cut':
            w(f'*{lines("Draft", c["draft"])} · cut*')
            w('')
            w('**Before**')
            w('')
            w(quote(c['before']))
            w('')
            w('**After:** cut.')
        else:
            w(f'*{lines("Draft", c["draft"])} → {lines("revised", c["rev"])}*')
            w('')
            w('**Before**')
            w('')
            w(quote(c['before']))
            w('')
            w('**After**')
            w('')
            w(quote(c['after']))
        w('')
        w(f'**Why.** {c["why"]}')
        if c.get('decision_note'):
            w('')
            w(f'**Your decision.** {c["decision_note"]}')
        elif c.get('call'):
            w('')
            w(f'**Your call.** {c["call"]}')

    new_chapter = '\n\n'.join(cur) + '\n'
    new_changes = '\n'.join(out) + '\n'
    if check:
        stale = [p.name for p, t in ((chapter_path, new_chapter), (out_path, new_changes))
                 if not p.exists() or p.read_text(encoding='utf-8') != t]
        print('Up to date.' if not stale else 'Out of date: ' + ', '.join(stale))
        sys.exit(1 if stale else 0)
    chapter_path.write_text(new_chapter, encoding='utf-8')
    out_path.write_text(new_changes, encoding='utf-8')
    print(f'{len(changes)} changes ({len(rejected)} rejected). Words {S0["words"]:,} -> {S1["words"]:,}. '
          f'Wrote "{chapter_path.name}" and "{out_path.name}".')


if __name__ == '__main__':
    main()
