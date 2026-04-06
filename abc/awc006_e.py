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
#=========================================================import heapq

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
N, Q = map(int,input().split())
S = list(map(int,input().split()))
fw = Fenwick_Tree(N)
for i in range(N):
    fw.add(i, S[i])

for i in range(Q):
    line = list(map(int, input().split()))
    
    if line[0] == 1:
        L, R = line[1], line[2]
        L -= 1
        R -= 1
        print(fw.sum(L, R))
        
    else:
        x, v = line[1], line[2]
        pre = S[x-1]
        fw.update(x-1, v, pre)
        S[x-1] = v


        