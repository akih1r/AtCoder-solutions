import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations
sys.setrecursionlimit(10**7)

N, M = map(int,input().split())
X, Y = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

cnt = 0
when = 0
where = "A"
while True:
    if where == "A":
        idx = bisect.bisect_left(A, when)
        if idx == N:
            break
        when = A[idx] + X
        where = "B"
    elif where == "B":
        idx = bisect.bisect_left(B, when)
        if idx == M:
            break
        when = B[idx] + Y 
        where = "A"
        cnt += 1

print(cnt)