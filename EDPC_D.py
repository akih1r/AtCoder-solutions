import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations
sys.setrecursionlimit(10**7)


N, W = map(int,input().split())
A = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(W+1) for _ in range(N+1)]


for i in range(1, N+1):
    w, v = A[i-1][0], A[i-1][1]
    for w_lim in range(W+1):
        
        
        dp[i][w_lim] = dp[i-1][w_lim]

       
        if w_lim >= w:
            if dp[i-1][w_lim - w] + v > dp[i][w_lim]:
                dp[i][w_lim] = dp[i-1][w_lim - w] + v

print(dp[N][W])
