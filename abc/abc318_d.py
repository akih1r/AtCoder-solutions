import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
from sortedcontainers import SortedSet, SortedList, SortedDict

#=======================================================
#
#N=int(input())
#A =list(map(int,input().split()))
#S = [0] + accmulate(A)
#ls = [list(map(int, input().split())) for _ in range(N)]
#grid = [list(input()) for _ in range(N)]
#alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#N, M, T = map(int,input().split())
#G = defaultdict(list)
#for i in range(M):
#    u, v = map(int,input().split())
#    G[u].append(v)
#    G[v].append(u)
#lst = sorted(lst, key=lambda x:x[1], reverse = True)
#=========================================================

"""
1. 目的
操作回数を最小に

2. それに関わる特徴、性質は？


3. 目的が達成するためにその性質をどう用いたら良いか？

4. 具体的にどう実装する？


"""

N = int(input())
D = [[0] * N for _ in range(N)]
for i in range(N - 1):
    row = list(map(int, input().split()))
    for k, d in enumerate(row):
        D[i][i + 1 + k] = d

full = 1 << N
dp = [0] * full

for S in range(full - 1):
    i = 0
    while S >> i & 1:      # S に入っていない最小の頂点
        i += 1

    T = S | 1 << i
    if dp[T] < dp[S]:      # i を余らせる
        dp[T] = dp[S]

    for j in range(i + 1, N):
        if S >> j & 1:
            continue
        U = T | 1 << j
        if dp[U] < dp[S] + D[i][j]:   # i と j を組ませる
            dp[U] = dp[S] + D[i][j]

print(dp[full - 1])