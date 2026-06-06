# 二次元累積和
H, W = map(int, input().split())
K = int(input())

# 文字列へのアクセスだけであれば list() 化しない方が少し高速です
grid = [input() for _ in range(H)]

# 0番目を0にするタイプの累積和リストを構築
acc_J = [[0] * (W + 1) for _ in range(H + 1)]
acc_O = [[0] * (W + 1) for _ in range(H + 1)]
acc_I = [[0] * (W + 1) for _ in range(H + 1)]

# 1回のループで J, O, I すべての累積和を同時に構築（高速化）
for i in range(H):
    for j in range(W):
        val_J = 1 if grid[i][j] == "J" else 0
        val_O = 1 if grid[i][j] == "O" else 0
        val_I = 1 if grid[i][j] == "I" else 0
        
        acc_J[i + 1][j + 1] = acc_J[i][j + 1] + acc_J[i + 1][j] - acc_J[i][j] + val_J
        acc_O[i + 1][j + 1] = acc_O[i][j + 1] + acc_O[i + 1][j] - acc_O[i][j] + val_O
        acc_I[i + 1][j + 1] = acc_I[i][j + 1] + acc_I[i + 1][j] - acc_I[i][j] + val_I

for _ in range(K):
    xl, yl, xr, yr = map(int, input().split())
    
    # sum2d を直書き（関数のオーバーヘッドをなくす）
    num_J = acc_J[xr][yr] - acc_J[xl - 1][yr] - acc_J[xr][yl - 1] + acc_J[xl - 1][yl - 1]
    num_O = acc_O[xr][yr] - acc_O[xl - 1][yr] - acc_O[xr][yl - 1] + acc_O[xl - 1][yl - 1]
    num_I = acc_I[xr][yr] - acc_I[xl - 1][yr] - acc_I[xr][yl - 1] + acc_I[xl - 1][yl - 1]
    
    print(*[num_J, num_O, num_I])