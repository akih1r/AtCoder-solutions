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

# 入力の受け取り
N, Q = map(int, input().split())
A = list(map(int, input().split()))
fw = Fenwick_Tree(N + 2)

for _ in range(Q):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        l = query[1] - 1
        r = query[2] - 1
        x = query[3]
        
        fw.add(l, x)
        fw.add(r + 1, -x)
        
    elif query[0] == 2:
        p = query[1] - 1
        
        ans = A[p] + fw.sum(0, p)
        print(ans)