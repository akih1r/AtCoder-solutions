import typing

import atcoder._bit


class LazySegTree:
    def __init__(
            self,
            op: typing.Callable[[typing.Any, typing.Any], typing.Any],
            e: typing.Any,
            mapping: typing.Callable[[typing.Any, typing.Any], typing.Any],
            composition: typing.Callable[[typing.Any, typing.Any], typing.Any],
            id_: typing.Any,
            v: typing.Union[int, typing.List[typing.Any]]) -> None:
        self._op = op
        self._e = e
        self._mapping = mapping
        self._composition = composition
        self._id = id_

        if isinstance(v, int):
            v = [e] * v

        self._n = len(v)
        self._log = atcoder._bit._ceil_pow2(self._n)
        self._size = 1 << self._log
        self._d = [e] * (2 * self._size)
        self._lz = [self._id] * self._size
        for i in range(self._n):
            self._d[self._size + i] = v[i]
        for i in range(self._size - 1, 0, -1):
            self._update(i)

    def set(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += self._size
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p: int) -> typing.Any:
        assert 0 <= p < self._n

        p += self._size
        for i in range(self._log, 0, -1):
            # 親から子に方向にpに関するlzでdを更新
            self._push(p >> i)
        return self._d[p]

    def prod(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n

        if left == right:
            return self._e

        left += self._size
        right += self._size

        for i in range(self._log, 0, -1):
            if ((left >> i) << i) != left:
                self._push(left >> i)
            if ((right >> i) << i) != right:
                self._push((right - 1) >> i)

        sml = self._e
        smr = self._e
        while left < right:
            if left & 1:
                sml = self._op(sml, self._d[left])
                left += 1
            if right & 1:
                right -= 1
                smr = self._op(self._d[right], smr)
            left >>= 1
            right >>= 1

        return self._op(sml, smr)

    def all_prod(self) -> typing.Any:
        return self._d[1]

    def apply(self, left: int, right: typing.Optional[int] = None,
              f: typing.Optional[typing.Any] = None) -> None:
        assert f is not None
        
        if right is None:
            #一点更新
            p = left
            assert 0 <= left < self._n

            p += self._size
            for i in range(self._log, 0, -1):
                #親から子へ残ってる遅延分を伝播
                self._push(p >> i)
            self._d[p] = self._mapping(f, self._d[p])
            for i in range(1, self._log + 1):
                # 子から親へ反映
                self._update(p >> i)
        else:
            # 区間更新
            assert 0 <= left <= right <= self._n
            if left == right:
                return

            left += self._size
            right += self._size

            for i in range(self._log, 0, -1):
                if ((left >> i) << i) != left:
                    # leftからi段上の先祖が持ってる一番左の葉がleftでないなら
                    self._push(left >> i)
                if ((right >> i) << i) != right:
                    self._push((right - 1) >> i)

            l2 = left
            r2 = right
            # 左右からlzまたはdをfで更新していく
            while left < right:
                if left & 1: 
                    self._all_apply(left, f)
                    left += 1
                if right & 1:
                    right -= 1 #先に隣に移動
                    self._all_apply(right, f)
                left >>= 1
                right >>= 1
            left = l2
            right = r2

            for i in range(1, self._log + 1):
                if ((left >> i) << i) != left:
                    self._update(left >> i)
                if ((right >> i) << i) != right:
                    self._update((right - 1) >> i)

    def max_right(
            self, left: int, g: typing.Callable[[typing.Any], bool]) -> int:
        assert 0 <= left <= self._n
        assert g(self._e)

        if left == self._n:
            return self._n

        left += self._size
        for i in range(self._log, 0, -1):
            self._push(left >> i)

        sm = self._e
        first = True
        while first or (left & -left) != left:
            first = False
            while left % 2 == 0:
                left >>= 1
            if not g(self._op(sm, self._d[left])):
                while left < self._size:
                    self._push(left)
                    left *= 2
                    if g(self._op(sm, self._d[left])):
                        sm = self._op(sm, self._d[left])
                        left += 1
                return left - self._size
            sm = self._op(sm, self._d[left])
            left += 1

        return self._n

    def min_left(self, right: int, g: typing.Any) -> int:
        assert 0 <= right <= self._n
        assert g(self._e)

        if right == 0:
            return 0

        right += self._size
        for i in range(self._log, 0, -1):
            self._push((right - 1) >> i)

        sm = self._e
        first = True
        while first or (right & -right) != right:
            first = False
            right -= 1
            while right > 1 and right % 2:
                right >>= 1
            if not g(self._op(self._d[right], sm)):
                while right < self._size:
                    self._push(right)
                    right = 2 * right + 1
                    if g(self._op(self._d[right], sm)):
                        sm = self._op(self._d[right], sm)
                        right -= 1
                return right + 1 - self._size
            sm = self._op(self._d[right], sm)

        return 0

    def _update(self, k: int) -> None:
        "子の二項演算結果を親へ反映"
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])

    def _all_apply(self, k: int, f: typing.Any) -> None:
        """
        d[k]をfで更新
        評価待ちのlz[k]と今来たfをどう作用させてlz[k]を更新させるかをcomposionに任せる
        """
        self._d[k] = self._mapping(f, self._d[k])
        if k < self._size:
            self._lz[k] = self._composition(f, self._lz[k]) # f = 新しい作用、g = 古い作用

    def _push(self, k: int) -> None:
        """
        kの子にlzを運搬 -> 子のdをそのlzで更新 -> 子のlzを更新
        """
        self._all_apply(2 * k, self._lz[k])
        self._all_apply(2 * k + 1, self._lz[k])
        self._lz[k] = self._id # リセット


"""
区間に作用させるとき:apply(l, r, f)
1点に作用させるとき:apply(p, f=x) と、f をキーワードで渡す

seg.set(p, x)	A[p] = x にする
seg.get(p)	A[p] を返す
seg.prod(l, r)	op(A[l], ..., A[r-1]) を返す。l == r なら e
seg.all_prod()	全体の op を返す
seg.apply(l, r, f)	A[l..r-1] に f をかける
seg.apply(p, f=f)	A[p] だけに f をかける。f はキーワードで渡す
seg.max_right(l, g)	g(prod(l, r)) が True のままでいられる最大の r を返す
seg.min_left(r, g)	g(prod(l, r)) が True のままでいられる最小の l を返す


op:_update と prod(子2つの値から親の値を作る)
mapping:_all_apply の1行目(ノードの値 d[k] を更新する)
composition:_all_apply の2行目(予約 lz[k] に新しい作用を重ねる)

apply(l,r,k)でどういう演算でk(kはi具体的な数字)をつかうのかをmappingがきめる
conpositonは新しい作用fと古い作用gがあったときに二つをあわせたときどうなるかを決める


区間に足す + 区間の和
seg = LazySegTree(
    lambda a, b: (a[0] + b[0], a[1] + b[1]),
    (0, 0),
    lambda f, x: (x[0] + f * x[1], x[1]),
    lambda f, g: f + g,
    0,
    [(a, 1) for a in A])
seg.apply(1, 4, 3)
print(seg.prod(0, 5)[0])   # 和は [0] で取り出す

区間に足す + 区間の最小値
INF = 1 << 60
seg = LazySegTree(
    min, INF,
    lambda f, x: f + x,
    lambda f, g: f + g,
    0,
    A)
seg.apply(2, 5, 10)      # A[2..4] に +10
print(seg.prod(0, 6))    # A[0..5] の最小値


区間を代入 + 区間の和
seg = LazySegTree(
    lambda a, b: (a[0] + b[0], a[1] + b[1]),
    (0, 0),
    lambda f, x: x if f is None else (f * x[1], x[1]),
    lambda f, g: g if f is None else f,
    None,
    [(a, 1) for a in A])
seg.apply(0, 3, 7)  
"""


