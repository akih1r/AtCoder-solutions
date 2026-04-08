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
#=========================================================import heapq




H, W = map(int,input().split())
grid = [0]+ [[0] + list(input()) for _ in range(H)]

dp = [[-1]* (W+1)for i in range(H+1)]
dp[0][0] = 0

for i in range(0,H):
    for j in range(0, W):
        if dp[i][j] == -1:
            continue
        
        #下
        dp[i+1][j] = max(dp[i][j]+ grid[i+1][j], dp[i+1][j])
        
        #右下
        if j+1 <= W:
            dp[i+1][j+1] = max(dp[i][j]+grid[i+1][j+1], dp[i+1][j+1])
        
        #左下
        if j-1 >= 1:
            dp[i+1][j-1] = max(dp[i][j]+grid[i+1][j-1], dp[i+1][j-1])