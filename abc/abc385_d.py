import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
from sortedcontainers import SortedSet, SortedList, SortedDict
input = sys.stdin.readline
#=======================================================
#
# N=int(input())
# A =list(map(int,input().split()))
# S = [0] + accmulate(A)
# ls = [list(map(int, input().split())) for _ in range(N)]
# grid = [list(input().rstrip()) for _ in range(N)]
# alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
# N, M, T = map(int,input().split())
# G = defaultdict(list)
# for i in range(M):
#     u, v = map(int,input().split())
#     G[u].append(v)
#     G[v].append(u)
# lst = sorted(lst, key=lambda x:x[1], reverse = True)
#=========================================================

"""
1 何ごとの話にすると見やすい？なにだけ持てばいい？
順序つきsetをつかうらしい

2 それについて、何がわかれば答えになる？


3 何を捨ててよく、なぜそれで足りる？何が効く？何が禁止？


4 その情報をそう更新/判定/集計すれば実装できる？

"""

import sys
from collections import defaultdict
from sortedcontainers import SortedList

def main():
    data = sys.stdin.buffer.read().split()
    p = 0
    N, M = int(data[p]), int(data[p+1]); p += 2
    sx, sy = int(data[p]), int(data[p+1]); p += 2

    xy = defaultdict(SortedList)   # x → その x にある y の SortedList
    yx = defaultdict(SortedList)   # y → その y にある x の SortedList

    for _ in range(N):
        x, y = int(data[p]), int(data[p+1]); p += 2
        xy[x].add(y)
        yx[y].add(x)

    res = 0
    for _ in range(M):
        d = data[p]; c = int(data[p+1]); p += 2

        x2, y2 = sx, sy
        if   d == b'U': y2 += c
        elif d == b'D': y2 -= c
        elif d == b'L': x2 -= c
        else:           x2 += c

        if sy == y2:
            # 横移動: y = sy 固定、x が [lo, hi]
            lo, hi = min(sx, x2), max(sx, x2)
            sl = yx.get(sy)
            if sl:
                i = sl.bisect_left(lo)
                while i < len(sl) and sl[i] <= hi:
                    x = sl.pop(i)      # yx[sy] から削除
                    xy[x].remove(sy)   # xy[x] からも削除
                    res += 1
        else:
            # 縦移動: x = sx 固定、y が [lo, hi]
            lo, hi = min(sy, y2), max(sy, y2)
            sl = xy.get(sx)
            if sl:
                i = sl.bisect_left(lo)
                while i < len(sl) and sl[i] <= hi:
                    y = sl.pop(i)      # xy[sx] から削除
                    yx[y].remove(sx)   # yx[y] からも削除
                    res += 1

        sx, sy = x2, y2

    print(sx, sy, res)

main()