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




import math

a, b = map(int, input().split())

f = lambda n: a / math.sqrt(n + 1) + b * n

argmin = int((a / (b * 2)) ** (2 / 3)) - 1
l = max(argmin - 5, 0)
r = min(argmin + 5, a // b)

ans = float(a)
for i in range(l, r + 1):
    ans = min(ans, f(i))

print(f"{ans:.10f}")