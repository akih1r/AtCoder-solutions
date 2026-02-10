import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
#N=int(input())
#N, K= map(int,input().split())
#D = list(map(int,input().split()))
#B = list(map(int,input().split()))

#ls = [list(map(int, input().split())) for _ in range(N)]
#grid = [list(input()) for _ in range(N)]
#alpha = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]


import heapq
G = defaultdict(list)
N = int(input())
for i in range(1, N-1+1):
    A, B, X = map(int,input().split())
    G[i].append((A, i+1))
    G[i].append((B, X))

hp = [(0, 1)]
dist = [10**18]*(N+1)
dist[1] = 0
while hp:
    d, now = heapq.heappop(hp)
    if d > dist[now]:
        continue
    
    for w, nxt in G[now]:
        if d + w < dist[nxt]:
            dist[nxt] = dist[now] + w
            heapq.heappush(hp, (dist[nxt], nxt))
        
print(dist[N])
    
    
    