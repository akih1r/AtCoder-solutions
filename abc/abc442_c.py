import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
#SN, M = map(int,input().split())
#S = list(input())
#A = list(map(int,input().split()))
#A, B, C, X, Y = map(int,input().split())

d= defaultdict(int)
N, M = map(int,input().split())
for i in range(M):
    a, b = map(int,input().split())
    d[a] += 1
    d[b] += 1
res = []
for i in range(1,N+1):
    Yes = d[i]
    No = N - Yes - 1
    if No >= 3:
        res.append((No * (No-1) * (No-2)) // 6)
    else:
        res.append(0)
print(*res)