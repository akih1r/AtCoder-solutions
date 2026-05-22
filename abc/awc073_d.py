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


N, M, K = map(int,input().split())
dist = [[float("inf")]*(M+1) for i in range(M+1)]
for i in range(K):
    u,v,w = map(int,input().split())
    dist[u][v] = w
    dist[v][u] = w
for i in range(1,M+1):
    for j in range(1,M+1):
        if i == j:
            dist[i][j] = 0

for k in range(1,M+1):
    for i in range(1,M+1):
        for j in range(1,M+1):
            dist[i][j] = min(dist[i][k]+dist[k][j], dist[i][j])

ans = 0
for i in range(N):
    s, t = map(int,input().split())
    ans += dist[s][t]
print(ans) 

    
    