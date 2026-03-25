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



N, M, K, T = map(int,input().split())
C = list(map(int,input().split()))
set_C = set(C)
G = defaultdict(list)
for i in range(M):
    u, v = map(int,input().split())
    G[u].append(v)
    G[v].append(u)
L = [0]*(N+1)
for i in range(1,N+1):
    if i in set_C:
        L[i] = T

stack = C
while stack:
    now = stack.pop()
    for nxt in G[now]:
        L[nxt] += 1
        if L[nxt] == T:
            stack.append(nxt)
cnt = 0
for i in range(1,N+1):
    if L[i] >= T:
        cnt += 1
print(cnt)