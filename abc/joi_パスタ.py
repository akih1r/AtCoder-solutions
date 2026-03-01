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


import sys

# 入力
N, K = map(int, input().split())

table = [0] * (N + 1)

for i in range(K):
    a, b = map(int, input().split())
    table[a] = b

# dp[i日目][最後に食べた料理(1-3)][連続回数(1-2)]
dp = [[[0] * 3 for _ in range(4)] for _ in range(N + 1)]

# 初期化：1日目の処理
# 1日目は「直前の料理」がないため、ループの外で特別扱いしたほうがバグが減ります
for dish in range(1, 4):
    # 1日目が固定されていて、その料理と違う場合はスキップ
    if table[1] != 0 and table[1] != dish:
        continue
    # 1日目は必ず「連続1回目」
    dp[1][dish][1] = 1

# DP遷移：1日目からN-1日目までループし、翌日(i+1)の状態を配る
for i in range(1, N):
    for dish in range(1, 4):        # 前日食べたパスタ
        for j in range(1, 3):       # 前日までの連続回数
            if dp[i][dish][j] == 0: # そもそもその状態がありえないならスキップ
                continue

            # 次の日(i+1日目)に食べるパスタ(next_dish)を全探索
            for next_dish in range(1, 4):
                
                # 制約チェック1: 予定表(table)と矛盾しないか
                if table[i+1] != 0 and table[i+1] != next_dish:
                    continue
                
                # 制約チェック2: 連続回数の更新
                if dish == next_dish:
                    next_j = j + 1
                else:
                    next_j = 1
                
                # 3回連続はダメなので、2回以下なら遷移可能
                if next_j <= 2:
                    dp[i+1][next_dish][next_j] += dp[i][dish][j]
                    dp[i+1][next_dish][next_j] %= 10000  # 問題文に合わせてMODをとる

ans = 0
for dish in range(1, 4):
    for j in range(1, 3):
        ans += dp[N][dish][j]

print(ans % 10000)