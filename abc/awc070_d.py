import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math

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
#
#=========================================================



N, M, Q = map(int, input().split())


B = [[0] * (M + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

imos = [[0] * (M + 2) for _ in range(N + 2)]

for _ in range(Q):
    r1, c1, r2, c2 = map(int, input().split())
    imos[r1][c1] += 1
    imos[r1][c2+1] -= 1
    imos[r2+1][c1] -= 1
    imos[r2+1][c2+1] += 1

# 累積和をとる
for i in range(1, N + 1):
    for j in range(1, M + 1):
        imos[i][j] += imos[i-1][j] + imos[i][j-1] - imos[i-1][j-1]

ans = 0
for i in range(1, N + 1):
    for j in range(1, M + 1):
        # 操作回数が奇数回なら
        if imos[i][j] % 2 != 0:
            br = 2 * B[i][j]
        # 偶数回（0回含む）なら
        else:
            br = B[i][j]
        ans += br

print(ans)