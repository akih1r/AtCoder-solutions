import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate, groupby
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
Diがボーナスステージのどれかにはいるかどうかをみたい
二分探索で愚直にいけない？
2 それについて、何がわかれば答えになる？


3 何を捨ててよく、なぜそれで足りる？何が効く？何が禁止？


4 その情報をそう更新/判定/集計すれば実装できる？

"""
N, M = map(int,input().split())
D = list(map(int,input().split()))
events = []
for i in range(M):
    l, r = map(int,input().split())
    events.append((l, 0))
    events.append((r + 1, 1))
events.sort()

xs = []
imos = [0]*(2*M + 1)#[)のimos
for i, (c, g) in enumerate(groupby(events, lambda x: x[0])):
    xs.append(c)
    for _, f in g:
        imos[i] += 1 if f == 0 else -1
imos = list(accumulate(imos))

ans = 0
for i in range(N):
    tmp = D[i]
    k = bisect.bisect_right(xs, D[i]) - 1
    if k >= 0 and imos[k] > 0:
        tmp *= 2
    ans += tmp
print(ans)