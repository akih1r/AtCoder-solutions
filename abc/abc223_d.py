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



N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
indeg = [0] * (N + 1) # 入次数

for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    indeg[v] += 1


que = []
for i in range(1, N + 1):
    if indeg[i] == 0:
        heapq.heappush(que, i)

res = []
while que:
    v = heapq.heappop(que)
    res.append(v)
    
    for nv in G[v]:
        indeg[nv] -= 1
        if indeg[nv] == 0:
            heapq.heappush(que, nv)

if len(res) == N:
    print(*res)
else:
    print(-1)