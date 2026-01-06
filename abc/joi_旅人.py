import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
N, M = map(int,input().split())
#S = list(input())
#A = list(map(int,input().split()))
#A, B, C, X, Y = map(int,input().split())


S = []
for i in range(N-1):
    s = int(input())
    S.append(s)

acc_S = [0] + list(accumulate(S))


A = []
for i in range(M):
    a = int(input())
    A.append(a)

where = 0
dist = 0
for i in range(M):
    dist += abs(acc_S[where+A[i]] - acc_S[where])
    dist %= 100000
    where += A[i]

print(dist)


