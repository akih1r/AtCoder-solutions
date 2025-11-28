import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations
sys.setrecursionlimit(10**7)


N = map(int,input().split())
A = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*3 for _ in range(N+1)]

#(i日目でｊを選んだときのｉ日目までの最大幸福度) = dp[i+1]

for i in range(N):
    for j in range(3):#前回の選択
        for k in range(3):#今回の選択
            if j == k:
                continue
            
            val = dp[i][j] + A[i][k]
            if dp[i+1][k] < val:
                dp[i+1][k] = val

print(max(dp[N]))