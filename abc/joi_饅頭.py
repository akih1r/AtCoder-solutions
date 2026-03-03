import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
#N=int(input())
#N, M= map(int,input().split())
#A = list(map(int,input().split()))
#ls = [list(map(int, input().split())) for _ in range(N)]
#grid = [list(input()) for _ in range(N)]
#alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#N, A = map(int,input().split())
#X = list(map(int,input().split()))

M, N = map(int, input().split())

A = [int(input()) for _ in range(M)]

A.sort(reverse=True)

profit = [0] * (M + 1)
for i in range(M):
    profit[i+1] = profit[i] + A[i]

INF = 1 << 60
C = [0] * N
E = [0] * N
for i in range(N):
    C[i], E[i] = map(int, input().split())


# dp[i][j] := i番目の箱までを考慮して、容量j以上を確保するための最小コスト
dp = [[INF] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 0


for i in range(N):
    for j in range(M + 1):
        if dp[i][j] == INF:
            continue
            
        #箱iを「買わない」場合
        if dp[i][j] < dp[i+1][j]:
            dp[i+1][j] = dp[i][j]
            
        #箱iを「買う」場合
        idx = min(j + C[i], M)
        if dp[i][j] + E[i] < dp[i+1][idx]:
            dp[i+1][idx] = dp[i][j] + E[i]

res = 0
for n in range(M + 1):
    if profit[n] - dp[N][n] > res:
        res = profit[n] - dp[N][n]

print(res)