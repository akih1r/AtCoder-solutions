import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math

#=======================================================
#
#N=int(input())
#A =list(map(int,input().split()))
#S = [0] + accmulate(A)
#ls = [list(map(int, input().split())) for _ in range(N)]
#grid = [list(input()) for _ in range(N)]
#alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#N, M, T = map(int,input().split())
#G = defaultdict(list)
#for i in range(M):
#    u, v = map(int,input().split())
#    G[u].append(v)
#    G[v].append(u)
#lst = sorted(lst, key=lambda x:x[1], reverse = True)
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
    

    def add_range(self, l, r, x):
        # [l, r] の閉区間（0-indexed）すべてに x を加算する（いもす法）
        # 内部の add メソッドを使い回す
        self.add(l, x)
        self.add(r + 1, -x)

    def get(self, p):
        # p番目(0-indexed)の「現在の値」を取得する
        # 区間加算（add_range）を使った場合は、このメソッドで値を取り出す
        return self._sum(p + 1)
    
    
    
#実際には消さず-d個していく
#すべてのマスに一個以上のブロックがつまれているのを確かめるために総和をつかう

#BIT[c個つまれてる] = なんか箇所あるか
#BIT[0] == 0ならブロックを取り除く
N, Q = map(int,input().split())
shift = 0
BIT = Fenwick_Tree(Q+2)
BIT.add(0, N)
#Block[i番目] = 何個
Block = [0]*(N)
for i in range(Q):
    num, x = map(int,input().split())
    if num == 1:
        old_c = Block[x - 1]
        Block[x - 1] += 1
        new_c = Block[x - 1]
        BIT.add(old_c, -1)
        BIT.add(new_c, 1)
        

        if BIT.sum(shift, shift) == 0:
            shift += 1
        
    else:
        y = x
        S = BIT.sum(y+shift, Q+1)
        print(S)
        
        

