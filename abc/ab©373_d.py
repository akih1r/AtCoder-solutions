import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
#N=int(input())
#N, T = map(int,input().split())
#A = list(map(int,input().split()))
#ls = [list(map(int, input().split())) for _ in range(N)]
#grid = [list(input()) for _ in range(N)]
#alpha = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    #ポテンシャル問題では逆も重みマイナスでつなぐ
    G[u].append((v, w))
    G[v].append((u,-w))

visited = set()
x = [0]*N

for start in range(N):
    if start in visited:
        continue
    stack = [start]
    visited.add(start)
    while stack:
        now = stack.pop()
        for nxt, w in G[now]:
            if nxt not in visited:
                visited.add(nxt)
                x[nxt] = w + x[now]
                stack.append(nxt)

print(*x)

        