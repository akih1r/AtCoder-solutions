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



N = int(input())
dp = [0]

for n in range(N):
    w, h, b = map(int, input().split())
    
    prev = dp
    M = len(prev)
    
    dp = [0] * (M + w)
    
    for i in range(M):
        # 頭に取り付ける（体の重さは変わらない）
        dp[i] = max(dp[i], prev[i] + h)
        
        # 体に取り付ける（体の重さが w 増える）
        dp[i + w] = max(dp[i + w], prev[i] + b)

# 条件（体の重さが半分以上）を満たす範囲から最大値を取得
half_index = len(dp) // 2
ans = max(dp[half_index:])

print(ans)