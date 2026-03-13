import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
#N=int(input())
#A = [0] + list(map(int,input().split()))
#ls = [list(map(int, input().split())) for _ in range(N)]
#grid = [list(input()) for _ in range(N)]
#alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#N, A = map(int,input().split())
#X = list(map(int,input().split()))

from collections import deque, defaultdict

N1, N2, M = map(int,input().split())
G = defaultdict(list)
for i in range(M):
    u, v = map(int,input().split())
    G[u].append(v)
    G[v].append(u)


def bfs(start, N):
    que = deque([start])
    dist = [-1]*(N+1)
    dist[start] = 0
    while que:
        now = que.popleft()
        for nxt in G[now]:
            if dist[nxt] == -1:
                dist[nxt] = dist[now]+1
                que.append(nxt)
    return dist


dist1 = bfs(1,N1)
dist2 = bfs(N1+N2, N1+N2)
print(max(dist1)+max(dist2)+1)