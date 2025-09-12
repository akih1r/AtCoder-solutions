import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations
sys.setrecursionlimit(10**7)

S = input().strip()
T = input().strip()

def rle(xs):
    if not xs:
        return []
    res = []
    cur, cnt = xs[0], 1
    for x in xs[1:]:
        if x == cur:
            cnt += 1
        else:
            res.append((cur, cnt))
            cur, cnt = x, 1
    res.append((cur, cnt))
    return res

RLE_S = rle(S)
RLE_T = rle(T)

ans = "Yes"
if len(RLE_S) != len(RLE_T):
    ans = "No"
for (cs, ns), (ct, nt) in zip(RLE_S, RLE_T):
    if cs != ct:
        ans = "No"
        continue
    if ns == 1:
        if nt != 1:
            ans = "No"
    else:
        if nt < ns:
            ans = "No"

print(ans)