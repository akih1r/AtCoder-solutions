import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
#N=int(input())
#N, M= map(int,input().split())
#A = list(map(int,input().split()))
#ls = [list(map(int, input().split())) for _ in range(N)]
#grid = [list(input()) for _ in range(N)]
#alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#N, A = map(int,input().split())
#X = list(map(int,input().split()))



import sys, bisect

# 入力
N, M = map(int, input().split())
P = []
for i in range(N):
    P.append(int(input()))

# 0点を追加することで「矢を投げない」という選択肢を表現する
P.append(0)

# 2本の矢の合計（S）をすべて列挙する
# 2本の合計を出しつつ、重複を削る
S = set()
for i in range(len(P)):
    for j in range(len(P)):
        val = P[i] + P[j]
        if val <= M:
            S.add(val)

# setからlistに変換してソート
S = sorted(list(S))

# 二分探索のためにソート
S.sort()

res = 0
# 1組目のペア（a）を固定し、M - a 以下の最大の2組目を二分探索で探す
for a in S:
    if a > M:
        continue
    
    # C++の upper_bound は Python の bisect_right に相当
    idx = bisect.bisect_right(S, M - a)
    
    if idx == 0:
        continue
    
    # idx-1 が、M - a を超えない最大値のインデックス
    val = S[idx - 1]
    if a + val > res:
        res = a + val

print(res)