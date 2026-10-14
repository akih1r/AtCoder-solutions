class BIT:
    def __init__(self, n):
        self._n = n
        self.data = [0] * (n + 1)

    def add(self, p, x):
        p += 1
        while p <= self._n:
            self.data[p] += x
            p += p & -p

    def _sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    def sum(self, l, r):          # [l, r) 半開区間
        return self._sum(r) - self._sum(l)

    def get(self, p):
        return self.sum(p, p + 1)


"""
作る（全部 0）	bit = BIT(N)	O(N)
作る（初期配列 A から）	for i, a in enumerate(A): bit.add(i, a)	O(N log N)
加算 A[p] += x	bit.add(p, x)	O(log N)
代入 A[p] = v	bit.add(p, v - bit.get(p))	O(log N)
1点取得 A[p]	bit.get(p)	O(log N)
区間和 sum(A[l:r])	bit.sum(l, r)	O(log N)
累積和 S[i]（A[0..i-1] の和）	bit.sum(0, i)	O(log N)
全体和	bit.sum(0, N)	O(log N)
空区間	bit.sum(l, l) → 0	—
"""


class BIT:
    """0-indexed の Fenwick Tree（点更新・区間和）"""

    def __init__(self, n_or_list):
        if isinstance(n_or_list, int):
            self._n = n_or_list
            self.data = [0] * (self._n + 1)
        else:                              # リストから O(n) で構築
            a = list(n_or_list)
            self._n = len(a)
            self.data = [0] + a
            for i in range(1, self._n + 1):
                j = i + (i & -i)
                if j <= self._n:
                    self.data[j] += self.data[i]

    def add(self, p, x):                   # a[p] += x   (0 <= p < n)
        assert 0 <= p < self._n
        p += 1
        while p <= self._n:
            self.data[p] += x
            p += p & -p

    def _sum(self, i):                     # a[0] + ... + a[i-1]
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

    def sum(self, l, r):                   # [l, r) 半開区間
        assert 0 <= l <= r <= self._n
        return self._sum(r) - self._sum(l)

    def get(self, p):                      # a[p]
        return self.sum(p, p + 1)

    def set(self, p, x):                   # a[p] = x
        self.add(p, x - self.get(p))

    def kth(self, k):
        """a が全て非負のとき、累積和が k 以上になる最小の添字を返す。
        k 番目(1-indexed)の要素の位置。全体和 < k なら n を返す。"""
        if k <= 0:
            return 0
        x = 0
        b = 1 << (self._n.bit_length())
        while b:
            if x + b <= self._n and self.data[x + b] < k:
                k -= self.data[x + b]
                x += b
            b >>= 1
        return x

"""
作る（全部 0）              bit = BIT(N)                  O(N)
作る（初期配列 A から）      bit = BIT(A)                  O(N)      ← 1つずつ add より速い
加算 A[p] += x             bit.add(p, x)                 O(log N)
代入 A[p] = v              bit.set(p, v)                 O(log N)
1点取得 A[p]               bit.get(p)                    O(log N)
区間和 sum(A[l:r])         bit.sum(l, r)                 O(log N)
累積和 S[i]（A[0..i-1]）    bit.sum(0, i)                 O(log N)
全体和                     bit.sum(0, N)                 O(log N)
空区間                     bit.sum(l, l) -> 0            —
k 番目の位置 (累積和が初めて k 以上になる位置)              bit.kth(k)                    O(log N)  ← A が全て非負のときのみ
要素数                     bit._n                        O(1)

添字は全て 0-indexed。p は 0 <= p < N、l, r は 0 <= l <= r <= N。
範囲外は assert で落ちる（add(N, x) が黙って無視されることはない）。

累積和が初めて k 以上になる位置
kth(k) の意味：sum(0, p) < k <= sum(0, p+1) となる最小の p を返す。
  ・集合を「その値の位置を 1」で管理していれば、k 番目に小さい要素の値が取れる
  ・kth(1) = 最小値の位置、kth(bit.sum(0, N)) = 最大値の位置
  ・k <= 0 なら 0、k が全体和より大きければ N が返る

値をそのまま添字に使うとき（転倒数・k 番目取得など）は
  ・値が 0..M なら BIT(M + 1)
  ・値が 1..M なら BIT(M + 1) にして add(v, 1)、または add(v - 1, 1)
  ・値が大きい / 負を含むなら座標圧縮する
"""