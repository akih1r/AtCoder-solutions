import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations
sys.setrecursionlimit(10**7)


N, Q = map(int,input().split())
hq = []
for i in range(1, N+1):
    heapq.heappush(hq, (i, 1))

for i in range(Q):
    X, Y = map(int,input().split())
    cnt = 0
    while hq:
        k, v  = heapq.heappop(hq)
        if k > X:
            heapq.heappush(hq, (k, v))
            break
        cnt += v
    heapq.heappush(hq, (Y, cnt))
    print(cnt)
