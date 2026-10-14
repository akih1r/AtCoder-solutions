def GridShow(grid):
    H = len(grid)
    for i in range(H):
        print(grid[i])

#転置
def transpose(A):
    """A: H*W の2次元リスト -> W*H の2次元リスト"""
    return [list(row) for row in zip(*A)]



#斜め抽出

# 右下→左上
rl_d = [[array[max(0, -d) + i][max(0, d) + i] for i in range(n - abs(d))] for d in range(1-n, n)]
print(rl_d)

# 左下→右上
lr_d = [[array[max(0, d) + i][min(n + d, n) - i - 1] for i in range(n - abs(d))] for d in range(1 - n, n)]
print(lr_d)