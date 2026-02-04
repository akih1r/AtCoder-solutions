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
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    #ポテンシャル問題では逆も重みマイナスでつなぐ
    G[u].append(v)
    G[v].append(u)

visited = set()
ans = 0
for start in range(N):
    if start in visited:
        continue
    stack = [start]
    visited.add(start)
    edge, node = 0, 1
    while stack:
        now = stack.pop()
        for nxt in G[now]:
            if nxt not in visited:
                visited.add(nxt)
                node += 1
                stack.append(nxt)
    ans += (node * (node -1) // 2)
    

print(ans-M)

        