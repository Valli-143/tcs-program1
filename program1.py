from collections import deque
import sys

def read_input():
    lines = [line.strip() for line in sys.stdin if line.strip()]
    for i, line in enumerate(lines):
        if line.isdigit():
            n = int(line)
            break
    else: return 0, [], []
    try:
        s, o = lines.index("shuffled", i+1)+1, lines.index("original", i+1)+1
        return n, lines[s:s+n], lines[o:o+n]
    except: return 0, [], []

def build_permutation(shuffled, original):
    pos, used, perm = {}, {}, []
    for i, v in enumerate(original): pos.setdefault(v, []).append(i)
    for v in shuffled:
        if v not in pos or used.get(v, 0) >= len(pos[v]): return None
        perm.append(pos[v][used.get(v, 0)])
        used[v] = used.get(v, 0) + 1
    return perm

def min_cut_insert(perm):
    start, target = tuple(perm), tuple(sorted(perm))
    if start == target: return 0
    q, seen = deque([start]), {start}
    steps = 0
    while q:
        for _ in range(len(q)):
            cur = q.popleft()
            for i in range(len(perm)):
                for j in range(i, len(perm)):
                    seg, rest = cur[i:j+1], cur[:i]+cur[j+1:]
                    for k in range(len(rest)+1):
                        if k == i: continue
                        new = tuple(rest[:k]+seg+rest[k:])
                        if new == target: return steps+1
                        if new not in seen:
                            seen.add(new)
                            q.append(new)
        steps += 1
    return -1

if __name__ == "__main__":
    n, shuffled, original = read_input()
    perm = build_permutation(shuffled, original)
    print(min_cut_insert(perm) if perm else 0)
