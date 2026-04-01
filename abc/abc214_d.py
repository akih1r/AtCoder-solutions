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


import sys

class UnionFind:
    def __init__(self, n):
        self.parents = [-1] * n
        # 各グループの辺の数を管理する配列
        self.edge_counts = [0] * n
        
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
            
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        if x == y:
            self.edge_counts[x] += 1
            return
        

        if -self.parents[x] < -self.parents[y]:
            x, y = y, x
        
        self.edge_counts[x] += self.edge_counts[y] + 1
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        
    def size(self, x):
        return -self.parents[self.find(x)]
    
    def edge_size(self, x):
        # 頂点xが含まれるグループの「辺の数」を返す
        return self.edge_counts[self.find(x)]

# ---------------------------------------------------------------------------------------------------

# 入力処理
line = input()
if line:
    N = int(line)
else:
    N = 0

edges = []
for i in range(N - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    edges.append((w, u, v))

# 重みの昇順にソート
edges.sort()

uf = UnionFind(N)
ans = 0

# 各辺について処理
for edge in edges:
    w, u, v = edge
    
    ans += w * uf.size(u) * uf.size(v)
    
    # 頂点を連結
    uf.union(u, v)

print(ans)
    