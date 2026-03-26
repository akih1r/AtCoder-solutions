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




N, K = map(int, input().split())
C = list(map(int, input().split()))

# dp[j] : 合計金額 j を作ることが可能かどうか（True/False）
# ここではビット演算を使って高速化します（dpの各ビットが金額に対応）
dp = 1  # 0ビット目が1（合計0が作れるという意味）

for x in C:
    # 現在作れる金額すべてに x を足したものを、新たな可能性として追加
    # (dp << x) は「今までの金額すべてに x を加算した状態」を作る
    dp |= (dp << x)

# K 以下の範囲で、ビットが立っている最大のインデックスを探す
# dp.bit_length() - 1 は立っている最大のビット（合計金額）を返しますが、
# K を超えている可能性があるので、マスク（制限）をかけます
mask = (1 << (K + 1)) - 1
possible_sums = dp & mask

# 最も右側（大きい方）のビットの位置が答え
print(possible_sums.bit_length() - 1)