import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
#N=int(input())
#A = [0] + list(map(int,input().split()))
#ls = [list(map(int, input().split())) for _ in range(N)]
#grid = [list(input()) for _ in range(N)]
#alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#N, A = map(int,input().split())
#X = list(map(int,input().split()))



X, Y, Z = map(int, input().split())
S = list(input())
N = len(S)

dp = [[float("inf")] * 2 for i in range(N + 1)]

dp[0][0] = 0
dp[0][1] = Z

for i in range(0, N):
    for j in range(0, 2):
        if dp[i][j] == float("inf"):
            continue
            
        if S[i] == "A":
            if j == 0:
                dp[i+1][0] = min(dp[i+1][0], dp[i][j] + Y)
                dp[i+1][1] = min(dp[i+1][1], dp[i][j] + Z + X, dp[i][j] + Y + Z)
            else:
                dp[i+1][1] = min(dp[i+1][1], dp[i][j] + X)
                dp[i+1][0] = min(dp[i+1][0], dp[i][j] + Z + Y, dp[i+1][1] + Z)
                
        if S[i] == "a":
            if j == 0:
                dp[i+1][0] = min(dp[i+1][0], dp[i][j] + X)
                dp[i+1][1] = min(dp[i+1][1], dp[i][j] + X + Z, dp[i][j] + Z + Y)
            else:
                dp[i+1][1] = min(dp[i+1][1], dp[i][j] + Y)
                dp[i+1][0] = min(dp[i+1][0], dp[i][j] + Y + Z, dp[i][j] + Z + X)

print(min(dp[N]))