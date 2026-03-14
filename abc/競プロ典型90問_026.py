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



N = int(input())
G = defaultdict(list)
for i in range(N-1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

color = [-1] * (N + 1)


stack = [1]
stack.append(1)
color[1] = 1

while stack:
    now = stack.pop()
    now_col = color[now]
    needed = 1 - now_col

    for nxt in G[now]:
        if color[nxt] == -1:
            color[nxt] = needed
            stack.append(nxt)

res0 = []
res1 = []
for i in range(1, N + 1):
    if color[i] == 0:
        res0.append(i)
    else:
        res1.append(i)


if len(res1) >= N // 2:
    ans = res1[:N // 2]
else:
    ans = res0[:N // 2]

print(*(ans))