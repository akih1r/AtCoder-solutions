from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, takewhile

# 累積max(左から)
def acc_max_L(A):
    return list(accumulate(A, max))

def acc_min_L(A):
    return list(accumulate(A, min))

def acc_max_R(A):
    A_rev = list(reversed(A))
    tmp = list(accumulate(A_rev, max)) 
    return list(reversed(tmp))

def acc_min_R(A):
    A_rev = list(reversed(A))
    tmp = list(accumulate(A_rev, min))
    return list(reversed(tmp))



# 二次元累積和
class PrefixSum2D:
    """0-indexed座標のグリッドに対する2次元累積和"""
    def __init__(self, H: int, W: int):
        self.H = H
        self.W = W
        # 元データ
        self.orig = [[0] * W for _ in range(H)]
        self.sums = [[0] * (W + 1) for _ in range(H + 1)]
        self.initialized = False
    
    def add(self, h: int, w: int, x: int) -> None:
        """(h, w)にxを加算します"""
        assert not self.initialized
        if 0 <= h < self.H and 0 <= w < self.W:
            self.orig[h][w] += x
    
    def set(self, h: int, w: int, x: int) -> None:
        """(h, w)にxを設定します"""
        assert not self.initialized
        if 0 <= h < self.H and 0 <= w < self.W:
            self.orig[h][w] = x
    
    def build(self) -> None:
        """2次元累積和の計算を行います"""
        assert not self.initialized
        for h in range(self.H):
            s = 0
            for w in range(self.W):
                s += self.orig[h][w]
                self.sums[h + 1][w + 1] = s + self.sums[h][w + 1]
        self.initialized = True
    
    def sum(self, u: int, l: int, d: int, r: int) -> int:
        """矩形 [u, d] * [l, r] の総和を返します"""
        assert self.initialized
        assert 0 <= u <= d < self.H
        assert 0 <= l <= r < self.W
        u1, l1, d1, r1 = u, l, d + 1, r + 1
        return self.sums[d1][r1] - self.sums[u1][r1] - self.sums[d1][l1] + self.sums[u1][l1]

    def getData(self) -> list[list[int]]:
        """元データを返却します"""
        return self.orig

    def getSumTable(self) -> list[list[int]]:
        """累積和テーブル（1-indexed）を返却します"""
        assert self.initialized
        return self.sums

    def __getitem__(self, h: int):
        return self.orig[h]

    @classmethod
    def makeData(cls, grid: list[list[int]]) -> "PrefixSum2D":
        """
        既存の2次元グリッドから累積和を構築します
        """
        H = len(grid)
        W = len(grid[0]) if H > 0 else 0
        obj = cls(H, W)
        for h in range(H):
            for w in range(W):
                obj.orig[h][w] = grid[h][w]
        obj.build()
        return obj


#同じ形のまま上から下に累積和
def accumulate_H(S):
    H = len(S)
    W = len(S[0])
    tate_acc = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            tate_acc[i][j] = (tate_acc[i - 1][j] if i else 0) + (S[i][j] == "#")



def GraphAccumulate(G:defaultdict):
    #重みで累積
    N = len(G)
    start = 1; sum_ = 0
    stack = [(start, sum_)]
    acc = [-1]*(N+1)
    acc[start] = 0
    visited = set([start])
    while stack:
        now, s = stack.pop()
        
        for nex, nw in G[now]:
            if nex not in visited:
                acc[nex] = s + nw
                stack.append((nex, acc[nex]))
                visited.add(nex)
    return acc


