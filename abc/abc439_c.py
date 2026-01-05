import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
#N = int(input())
#A = list(map(int,input().split()))
#N, M = map(int,input().split())
N = int(input())
bo = [0]*(N+1)

nr = math.ceil(N ** 0.5)
xy = defaultdict(int)
for x in range(1,nr):
    for y in range(x+1,nr+1):
        v = x**2 + y **2
        if v > N:
            break
        bo[v] += 1

k = 0
res = []
for n in range(1, N+1):
    if bo[n] == 1:
        k += 1
        res.append(n)
print(k)
print(*res)
    