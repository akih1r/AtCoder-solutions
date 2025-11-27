import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations
sys.setrecursionlimit(10**7)


N = int(input())
H = list(map(int,input().split()))

dp = [float('inf')]*N
dp[0] = 0

for i in range(1,N):
    if i == 1:
        dp[i] = abs(H[i]-H[i-1])
        continue
    dp[i] = min(dp[i-1]+ abs(H[i] - H[i-1]) ,
                             dp[i-2] + abs(H[i] - H[i-2]))

print(dp[N-1])