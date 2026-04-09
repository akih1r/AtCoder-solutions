
#=========================================================
# 0-indexed で引数を受け取り、内部で 1-indexed に変換するクラス
#=========================================================

class Fenwick_Tree:
    def __init__(self, n):
        self._n = n
        # 内部は 1-indexed 用にサイズ n+1
        self.data = [0] * (n + 1)
    
    def add(self, p, x):
        # p番目(0-indexed)にxを加算
        idx = p + 1
        while idx <= self._n:
            self.data[idx] += x
            idx += idx & -idx
    
    def update(self, p, x, pre):
        # p番目の値をpreからxに変更
        self.add(p, x - pre)
        #メイン関数で以下のようにするひつようがある
        #pre = A[0_idx]
        #fw.update(0_idx, after, pre)
        #A[x-1] = after
        
        
    
    def sum(self, l, r):
        # [l, r] の閉区間（0-indexed）の和を求める
        # 内部計算用にそれぞれ +1 する
        l_idx = l + 1
        r_idx = r + 1
        if l_idx > r_idx: return 0
        return self._sum(r_idx) - self._sum(l_idx - 1)
    
    def _sum(self, i):
        # 1 から i までの累積和
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & -i
        return s

#=========================================================
# メイン処理（直書き）
#=========================================================

line1 = input().split()
if line1:
    N, Q = map(int, line1)
    fw = Fenwick_Tree(N)

    for i in range(Q):
        line = list(map(int, input().split()))
        if not line: continue
        
        if line[0] == 1:
            # クエリ1: A[pos] = x (posは1-indexed)
            # クラスには 0-indexed で渡すため -1 する
            pos_0 = line[1] - 1
            x = line[2]
            
            # 現在の値を取得（0-indexedで指定）
            pre = fw.sum(pos_0, pos_0)
            fw.add(pos_0, x, pre)
            
        else:
            # クエリ2: A[l] から A[r-1] までの和
            # l, r は 1-indexed で与えられる
            # 0-indexed に直すと、インデックスは (l-1) から (r-2) まで
            l_0 = line[1] - 1
            r_0 = line[2] - 2
            
            # クラスには 0-indexed の範囲 [l_0, r_0] を渡す
            print(fw.sum(l_0, r_0))