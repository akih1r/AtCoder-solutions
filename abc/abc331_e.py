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

import heapq

# 入力の読み込み
line1 = input().split()

N, M, L = map(int, line1)

# (値, 元のインデックス) の形で保持
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = []
for i in range(N):
    a.append((A[i], i))
    
b = []
for i in range(M):
    b.append((B[i], i))

a.sort(key=lambda x: x[0], reverse=True)
b.sort(key=lambda x: x[0], reverse=True)

bad = set()
for _ in range(L):
    c, d = map(int, input().split())
    bad.add((c - 1, d - 1))


Q = [(-(a[0][0] + b[0][0]), 0, 0)]
visited = {(0, 0)}

while Q:
    neg_cost, i, j = heapq.heappop(Q)
    cost = -neg_cost
    
    # a[i] と b[j] の元のインデックスを取得してチェック
    orig_idx_a = a[i][1]
    orig_idx_b = b[j][1]
    
    if (orig_idx_a, orig_idx_b) not in bad:
        print(cost)
        break
    
    # 次の候補（aを一つ進める、またはbを一つ進める）をキューに追加
    # 1. aのインデックスを増やす
    if i + 1 < N and (i + 1, j) not in visited:
        visited.add((i + 1, j))
        next_score = a[i + 1][0] + b[j][0]
        heapq.heappush(Q, (-next_score, i + 1, j))
        
    # 2. bのインデックスを増やす
    if j + 1 < M and (i, j + 1) not in visited:
        visited.add((i, j + 1))
        next_score = a[i][0] + b[j + 1][0]
        heapq.heappush(Q, (-next_score, i, j + 1))