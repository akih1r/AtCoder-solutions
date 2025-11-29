import sys

# 入力高速化
input = sys.stdin.readline

# 定数
INF = 1 << 60
MAX_V = 100100

# 入力
N, W = map(int, input().split())

weights = []
values = []
for _ in range(N):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

# DPテーブル初期化
# dp[i][j]: i番目まで見て、価値の総和がjになるときの「最小の重さ」
dp = [[INF] * MAX_V for _ in range(N + 1)]


dp[0][0] = 0


for i in range(N):
    w = weights[i]
    v = values[i]
    
    for sum_v in range(MAX_V):
        
        # i番目の品物を選ぶ場合
        if sum_v - v >= 0:
            if dp[i][sum_v - v] + w < dp[i+1][sum_v]:
                dp[i+1][sum_v] = dp[i][sum_v - v] + w
        
        # i番目の品物を選ばない場合
        if dp[i][sum_v] < dp[i+1][sum_v]:
            dp[i+1][sum_v] = dp[i][sum_v]


res = 0
for sum_v in range(MAX_V):
    if dp[N][sum_v] <= W:
        res = sum_v

print(res)
