import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
#N=int(input())
#N, M= map(int,input().split())
#A = [0] + list(map(int,input().split()))
#ls = [list(map(int, input().split())) for _ in range(N)]
#grid = [list(input()) for _ in range(N)]
#alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


import sys


S = input()
N = len(S)
T = "chokudai"
M = len(T)
MOD = 10**9 + 7


dp = [[0] * (M + 1) for _ in range(N + 1)]


dp[0][0] = 1

for i in range(0, N):
    for j in range(0, M+1):
        # 今の値が0なら配る意味がないのでスキップ（枝刈り）
        if dp[i][j] == 0:
            continue

        dp[i+1][j] += dp[i][j]
        dp[i+1][j] %= MOD

        if j < M and S[i] == T[j]:
            dp[i+1][j+1] += dp[i][j]
            dp[i+1][j+1] %= MOD

print(dp[N][M])
    