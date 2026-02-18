import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
#N=int(input())
#N, M= map(int,input().split())

#A = [0] + list(map(int,input().split()))

#ls = [list(map(int, input().split())) for _ in range(N)]
#grid = [list(input()) for _ in range(N)]
#alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

N, Q = map(int,input().split())

G = defaultdict(list)
for i in range(N-1):
    u, v = map(int,input().split())
    G[u].append(v)
    G[v].append(u)

#色をつける
stack = []
color = [-1]*(N+1)
stack.append(1)
color[1] = 0
while stack:
    now = stack.pop()
    expected = 1 - color[now]
    for nxt in G[now]:
        if color[nxt] == -1:
            color[nxt] = expected
            stack.append(nxt)
            
        
for _ in range(Q):
    c, d = map(int, input().split())
    if color[c] == color[d]:
        print("Town")
    else:
        print("Road")
