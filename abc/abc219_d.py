import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math

#=======================================================
#
#N=int(input())
#A =list(map(int,input().split()))
#S = [0] + accmulate(A)
#ls = [list(map(int, input().split())) for _ in range(N)]
#grid = [list(input()) for _ in range(N)]
#alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#N, M, T = map(int,input().split())
#G = defaultdict(list)
#for i in range(M):
#    u, v = map(int,input().split())
#    G[u].append(v)
#    G[v].append(u)
#
#=========================================================

MOD = 998244353

s = input()
n = len(s)

# dp[i][j]: i文字目まで処理して、累積の括弧のバランス（開き括弧の数）がjである状態数
dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if dp[i][j] == 0:
            continue
        
        # 現在の文字が ')' でないなら、開き括弧として扱えるためバランスを +1
        if s[i] != ')':
            dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j]) % MOD
            
        # 現在の文字が '(' でなく、かつバランスが 0 でないなら、閉じ括弧として扱えるためバランスを -1
        if j != 0 and s[i] != '(':
            dp[i + 1][j - 1] = (dp[i + 1][j - 1] + dp[i][j]) % MOD

print(dp[n][0])