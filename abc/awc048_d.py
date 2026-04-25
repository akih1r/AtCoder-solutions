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
#=========================================================import heapq



from itertools import accumulate

def sum2d(xl, yl, xr, yr, s):
    res = 0
    res += s[xr][yr]
    res -= s[xl - 1][yr]
    res -= s[xr][yl - 1]
    res += s[xl - 1][yl - 1]
    return res

N, M, K = map(int, input().split())

# 0行目
s = [[0] * (M + 1)]

for _ in range(N):
    S = input()
    s.append([0] + list(accumulate(int(x) for x in S)))

# 縦方向の累積和はループで処理
for i in range(1, N + 1):
    for j in range(1, M + 1):
        s[i][j] += s[i - 1][j]

vp = []
for h in range(1, 201):
    if K % h == 0 and (K // h) <= 200:
        vp.append((h, K // h))

res = -1
for i in range(1, N + 1):
    for j in range(1, M + 1):
        for nx in vp:
            ir = i + nx[0] - 1
            jr = j + nx[1] - 1
            if ir <= N and jr <= M:
                res = max(res, sum2d(i, j, ir, jr, s))

print(res)