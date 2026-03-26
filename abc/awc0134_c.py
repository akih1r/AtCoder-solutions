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


# 入力の受け取り
n, k, t, c = map(int, input().split())
a = list(map(int, input().split()))

# 変数の初期化
water = 0
res = 0
# 余裕を持たせたサイズの配列を作成
finish = [0] * (n + k + 5)

# 各花壇を左から順に処理
for i in range(n):
    # この地点で効果が切れる操作分を減らす
    water -= finish[i]
    
    # 目標 T に届くために、この地点から新しく開始すべき操作回数を計算
    # 0未満にならないよう max(0, ...) を使用
    start = max(0, t - a[i] - water)
    
    res += start
    water += start
    # i + k 番目の地点で、今回開始した start 回分の効果が切れるように記録
    finish[i + k] += start

# 合計コストを出力
print(res * c)