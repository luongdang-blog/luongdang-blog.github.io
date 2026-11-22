import json, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
P = lambda f: os.path.join(HERE, f)
from datetime import datetime

songs, seen, n = [], set(), 0
for line in open(P('data.tsv'), encoding='utf-8'):
    line = line.rstrip('\n')
    if not line.strip():
        continue
    parts = (line.split('\t') + ['', ''])[:3]
    vid, title, ch = [p.strip() for p in parts]
    if vid in seen:
        continue
    seen.add(vid)
    if vid.startswith('CHANNEL:'):
        songs.append({'special': True, 'url': 'https://www.youtube.com/' + vid[8:] + '/videos',
                      'title': title, 'sub': 'Bấm để xem toàn bộ video của kênh', 'ch': ch})
        continue
    n += 1
    url = 'https://www.youtube.com/watch?v=' + vid
    if not title:
        title, sub, ch = 'Video trên YouTube', '(Chưa đọc được tên bài – bấm để nghe)', ch or 'Chưa rõ kênh'
    else:
        segs = [s.strip() for s in title.split(' | ') if s.strip()]
        title, sub = segs[0], ' · '.join(segs[1:])
    songs.append({'n': n, 'url': url, 'title': title, 'sub': sub, 'ch': ch})


import unicodedata, re
VN = 'a ă â b c d đ e ê f g h i j k l m n o ô ơ p q r s t u ư v w x y z'.split()
RANK = {c:i for i,c in enumerate(VN)}
def letter_key(ch):
    d = unicodedata.normalize('NFD', ch.lower())
    base = d[0]
    if base == 'đ': return 100+RANK['đ']
    if '\u0306' in d and base=='a': base='ă'
    elif '\u0302' in d and base in 'aeo': base={'a':'â','e':'ê','o':'ô'}[base]
    elif '\u031b' in d and base in 'ou': base={'o':'ơ','u':'ư'}[base]
    if base in RANK: return 100+RANK[base]
    if base.isdigit(): return 10+int(base)
    return 0
def vn_key(s):
    s = re.sub(r'^[^0-9A-Za-zÀ-ỹĐđ]+', '', s)
    return [letter_key(c) for c in s if c.isalnum() or c==' '] , s.lower()
BKT = 'bài không tên'
def is_bkt(s): return s['title'].lower().startswith(BKT)
main = sorted([s for s in songs if not is_bkt(s)], key=lambda s: vn_key(s['title']))
tail = [s for s in songs if is_bkt(s)]   # loạt "Bài Không Tên" giữ cuối, theo thứ tự trong data.tsv
songs = main + tail
for i, s in enumerate(songs, 1): s['n'] = i

updated = sys.argv[1] if len(sys.argv) > 1 else datetime.now().strftime('%d/%m/%Y')
html = open(P('template.html'), encoding='utf-8').read()
html = html.replace('__COUNT__', str(len(songs))).replace('__VER__', datetime.now().strftime('%Y%m%d%H%M'))
html = html.replace('__DATA__', json.dumps(songs, ensure_ascii=False).replace('</', '<\\/')).replace('__UPDATED__', updated)
open(sys.argv[2] if len(sys.argv) > 2 else P('index.html'), 'w', encoding='utf-8').write(html)
print(n, 'songs,', len(songs), 'cards')
