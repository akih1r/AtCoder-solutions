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

N, M = map(int,input().split())
G = defaultdict(list)
for i in range(M):
    a, b = map(int,input().split())
    G[a].append(b)
    G[b].append(a)

visited = set()
stack = [(1,0)]
path = []
while stack:
    now, state = stack.pop()
    if state == 0:
        if now in visited:
            continue
        visited.add(now)
        path.append(now)
        
        if now == N:
            ans = path
            break
        
        stack.append((now,1))
        for nxt in G[now]:
            if nxt not in visited:
                stack.append((nxt,0))
    else:
        path.pop()

print(*path)