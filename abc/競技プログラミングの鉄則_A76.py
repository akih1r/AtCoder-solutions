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
#
#=========================================================

import bisect

#=========================================================
# 0-indexed で引数を受け取り、内部で 1-indexed に変換するクラス
# 今回は「区間加算・一点取得」用にカスタマイズ
#=========================================================
class Fenwick_Tree:
    def __init__(self, n):
        self._n = n
        self.data = [0] * (n + 1)
        self.MOD = 10**9 + 7
    
    def add(self, p, x):
        # p番目(0-indexed)にxを加算
        # マイナスの値が来てもPythonの剰余はよしなに処理してくれます
        idx = p + 1
        while idx <= self._n:
            self.data[idx] = (self.data[idx] + x) % self.MOD
            idx += idx & -idx
    
    def point_query(self, p):
        # 0番目からp番目までの累積和を返す
        # 差分（いもす法）の累積和をとることで、その地点の「現在の値」になる
        return self._sum(p + 1)
    
    def _sum(self, i):
        s = 0
        while i > 0:
            s = (s + self.data[i]) % self.MOD
            i -= i & -i
        return s


N, W, L, R = map(int, input().split())
X = list(map(int, input().split()))


P = [0] + X + [W]
n_all = len(P)

fw = Fenwick_Tree(n_all + 1)


fw.add(0, 1)
fw.add(1, -1)

for i in range(n_all):
    # まず、今いる地点 i の値を確定させる（一点取得）
    dp_i = fw.point_query(i)
    
    if dp_i == 0:
        continue
        
    left_coord = P[i] + L
    right_coord = P[i] + R
    
    # 二分探索でインデックスの範囲 [l, r] を特定
    l = bisect.bisect_left(P, left_coord)
    r = bisect.bisect_right(P, right_coord) - 1
    
    if l <= r:
        # 区間 [l, r] のすべてに dp_i を配る（いもす法による区間加算）
        fw.add(l, dp_i)
        fw.add(r + 1, -dp_i)


print(fw.point_query(n_all - 1))