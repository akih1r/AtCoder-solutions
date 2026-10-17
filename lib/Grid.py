def GridShow(grid):
    H = len(grid)
    for i in range(H):
        print(grid[i])

#転置
def transpose(A):
    """A: H*W の2次元リスト -> W*H の2次元リスト"""
    return [list(row) for row in zip(*A)]



#斜め抽出

# \ 向きの斜め線（d = 列 − 行）
# 線の並び: 左下の角 → 右上の角
# 線の中:   左上 → 右下
def rl_diagonals(array):
    n = len(array)
    return [[array[max(0, -d) + i][max(0, d) + i] for i in range(n - abs(d))] for d in range(1 - n, n)]

# / 向きの斜め線（行 + 列 = d + n - 1）
# 線の並び: 左上の角 → 右下の角
# 線の中:   右上 → 左下
def lr_diagonals(array):
    n = len(array)
    return [[array[max(0, d) + i][min(n + d, n) - i - 1] for i in range(n - abs(d))] for d in range(1 - n, n)]

#array =
#1 2 3
#4 5 6
#7 8 9
#rl_diagonals → [[7], [4, 8], [1, 5, 9], [2, 6], [3]]
#lr_diagonals → [[1], [2, 4], [3, 5, 7], [6, 8], [9]]