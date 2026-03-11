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
#N, A = map(int,input().split())
#X = list(map(int,input().split()))




N = int(input())
snuke_map = {}
max_t = 0
for _ in range(N):
    t, x, a = map(int, input().split())
    snuke_map[(t, x)] = a
    if t > max_t:
        max_t = t

dp = [[-1] * 5 for _ in range(max_t + 1)]

# 初期状態（時刻 0, 座標 0）
dp[0][0] = 0
if (0, 0) in snuke_map:
    dp[0][0] = snuke_map[(0, 0)]


for t in range(max_t):
    for x in range(5):
        if dp[t][x] == -1:
            continue
        
        # 次の時刻 t+1 で移動できる範囲は x-1, x, x+1
        for dx in range(-1, 2):
            next_x = x + dx
            
            if 0 <= next_x <= 4:
                gain = snuke_map.get((t + 1, next_x), 0)
                dp[t+1][next_x] = max(dp[t][x]+gain, dp[t+1][next_x])

ans = 0
for x in range(5):
    if dp[max_t][x] > ans:
        ans = dp[max_t][x]

print(ans)