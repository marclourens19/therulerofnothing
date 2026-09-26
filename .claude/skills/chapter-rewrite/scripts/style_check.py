#!/usr/bin/env python3
"""Mechanical style check for a chapter of The Ruler of Nothing.

Usage:
    python3 style_check.py "<chapter>.md"

It reports what a script can count. It doesn't judge anything: each hit is a place to
look, not an automatic fix. Oaths, gestures and "nothing" are allowed; the counts show
where they cluster. The house rules behind each check are in SKILL.md and in the design
bible (section 2.3) and the old Craft Rules (section 4).
"""
import re
import statistics
import sys
from collections import defaultdict

US_SPELLINGS = r'\b(toward|afterward|color\w*|armor\w*|gray|center\w*|favor\w*|honor\w*|neighbor\w*|' \
               r'labor\w*|harbor\w*|odor\w*|vapor\w*|rumor\w*|valor|splendor|traveled|traveling|traveler\w*|' \
               r'canceled|jewelry|plow\w*|skeptic\w*|defense|offense|analyz\w*|paralyz\w*)\b'
IZE_OK = {'size', 'sizes', 'sized', 'prize', 'prizes', 'prized', 'seize', 'seizes', 'seized', 'seizing',
          'capsize', 'capsized', 'baize', 'maize', 'citizen', 'citizens', 'downsize', 'oversize', 'oversized'}
OATHS = r'by the four\b|by the eight\b|before the eight|four preserve \w+|last dark take \w+|in the last dark|' \
        r'\bshite?\b|\bdamn\w*'
FINGERPRINTS = {
    '"not X, but Y"': r'\bnot\b[^.!?"]{1,60}, but\b',
    '"for a moment"': r'\bfor (a|one) moment\b',
    '"nothing answered"': r'\bnothing\b[^.!?]{0,20}\banswer',
    '"almost heard"': r'\balmost heard\b',
}
GESTURES = {
    'eyes and gaze': r"\b(eyes|gaze|glance[sd]?|stared|looked (down|away|up))\b",
    'hands and fingers': r'\b(hands?|fingers?|fists?|grip)\b',
    'breath': r'\bbreath(s|ed|ing)?\b',
    'jaw and mouth': r'\b(jaw|mouth|lips)\b',
    'shoulders': r'\bshoulders?\b',
    'silence and stillness': r'\b(silence|silent|went still|stillness)\b',
}


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    text = open(sys.argv[1], encoding='utf-8').read()
    lines = text.split('\n')
    body = [(i + 1, l) for i, l in enumerate(lines) if l.strip() and not l.startswith('# ')]
    prose = [(n, l) for n, l in body if l.strip() != '---']

    def report(title, hits, limit=40):
        print(f'\n== {title}: {len(hits)}')
        for n, s in hits[:limit]:
            print(f'   {n}: {s}')
        if len(hits) > limit:
            print(f'   … and {len(hits) - limit} more')

    def grep(pattern, flags=re.I):
        hits = []
        for n, l in prose:
            for m in re.finditer(pattern, l, flags):
                hits.append((n, m.group(0)))
        return hits

    # Typography
    report('American spellings', grep(US_SPELLINGS))
    report('-ize spellings (British house style uses -ise)',
           [h for h in grep(r'\b\w+iz(e|es|ed|ing)\b') if h[1].lower() not in IZE_OK])
    report('Spaced or doubled dashes (use an em dash with no spaces)', grep(r' [—–-] |—\s|\s—|――|ーー|(?<!-)--(?!-)'))
    report('Three dots (use the single … character)', grep(r'\.\.\.'))
    report('Curly quotes (the chapters use straight quotes)', grep('[“”‘’]'))
    report('Double spaces', grep(r'\S  +\S'))
    bold = grep(r'\*\*[^*]+\*\*')
    report('Bold other than THOOM (bold is for THOOM and rare purposeful sounds)',
           [h for h in bold if h[1] != '**THOOM.**'])
    report('THOOM (belongs only to his heartbeat)', [h for h in bold if 'THOOM' in h[1]])
    report('Italics (immediate thought or precise stress only)', grep(r'(?<!\*)\*[^*\n]+\*(?!\*)'), limit=60)
    report('Corner brackets', grep(r'『[^』]*』'))
    report('Section breaks (---: only for a real shift of time, place or viewpoint)',
           [(n, l) for n, l in body if l.strip() == '---'])

    # Words that cluster
    report('Oaths and swearing (sparingly; vary them)', grep(OATHS))
    nothing = grep(r'\bnothing\b')
    print(f'\n== "nothing" (the title word: keep it rare): {len(nothing)}')
    print('   lines: ' + ', '.join(str(n) for n, _ in nothing))
    for name, pat in FINGERPRINTS.items():
        report(f'Fingerprint phrase {name}', grep(pat))

    print('\n== Gesture counts (watch for the same one close together)')
    for name, pat in GESTURES.items():
        hits = grep(pat)
        close = []
        for (a, _), (b, _) in zip(hits, hits[1:]):
            if 0 < b - a <= 6:
                close.append(f'{a}/{b}')
        print(f'   {name}: {len(hits)}' + (f'  (within 6 lines of each other at {", ".join(close[:12])})' if close else ''))

    # Exact repeats: the same run of 6 words in two places
    words_at = defaultdict(list)
    for n, l in body:
        toks = re.findall(r"[a-z']+", l.lower())
        for k in range(len(toks) - 5):
            words_at[' '.join(toks[k:k + 6])].append(n)
    repeats = sorted({(v[0], f'"{g}" also at line {", ".join(map(str, sorted(set(v[1:]))))}')
                      for g, v in words_at.items() if len(set(v)) > 1})
    report('Repeated six-word runs (exact repeats across the chapter)', repeats)

    # Paragraph rhythm
    paras = [(n, l) for n, l in body if l.strip() != '---']
    wc = [len(l.split()) for _, l in paras]
    print('\n== Paragraph rhythm')
    print(f'   paragraphs: {len(paras)}, words: {sum(wc):,}, median paragraph: {statistics.median(wc):g} words '
          f'(house target roughly 14–22)')
    print(f'   paragraphs of five words or fewer: {sum(1 for x in wc if x <= 5)} '
          '(each should be a real narrowing of attention)')
    longest = sorted(zip(wc, [n for n, _ in paras]), reverse=True)[:5]
    print('   longest paragraphs: ' + ', '.join(f'line {n} ({c} words)' for c, n in longest))

    # Speaker clarity: runs of three or more lines of pure dialogue, with no tag or action
    runs, run = [], []
    for n, l in paras:
        if l.startswith('"') and not re.sub(r'"[^"]*"', '', l).strip(' .,;:!?—…'):
            run.append(n)
            continue
        if len(run) >= 3:
            runs.append((run[0], f'{len(run)} untagged lines in a row, ending at line {run[-1]}'))
        run = []
    if len(run) >= 3:
        runs.append((run[0], f'{len(run)} untagged lines in a row, ending at line {run[-1]}'))
    report('Runs of untagged dialogue (re-anchor the speaker if it could be unclear)', runs)

if __name__ == '__main__':
    main()
