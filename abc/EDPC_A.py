import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations
sys.setrecursionlimit(10**7)

#一次元DP
#貰うDP
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

#配るDP

for i in range(N):
        
        # 1つ先へ配る (行き先がゴール以下である場合のみ)
        if i + 1 < N:
            # dp[i+1] = min(現在のdp[i+1], 今の場所までのコスト + ジャンプコスト)
            dp[i + 1] = min(dp[i + 1], dp[i] + abs(H[i] - H[i + 1]))

        # 2つ先へ配る (行き先がゴール以下である場合のみ)
        if i + 2 < N:
            dp[i + 2] = min(dp[i + 2], dp[i] + abs(H[i] - H[i + 2]))

    
print(dp[N - 1])

