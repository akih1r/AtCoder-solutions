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



N, Q = map(int, input().split())
S = input()

# ローリングハッシュの設定
MOD = (1 << 61) - 1
BASE = 10**5 + 7 # 適当な基数

# 前計算: 累乗と累積ハッシュ
power = [1] * (N + 1)
hash_val = [0] * (N + 1)

for i in range(N):
    power[i + 1] = (power[i] * BASE) % MOD
    hash_val[i + 1] = (hash_val[i] * BASE + ord(S[i])) % MOD

# クエリ処理
for _ in range(Q):
    a, b, c, d = map(int, input().split())
    
    # S[a, b] のハッシュ値計算 (1-indexed)
    # 長さは b - a + 1
    len_ab = b - a + 1
    h_ab = (hash_val[b] - hash_val[a - 1] * power[len_ab]) % MOD
    
    # S[c, d] のハッシュ値計算
    len_cd = d - c + 1
    h_cd = (hash_val[d] - hash_val[c - 1] * power[len_cd]) % MOD
    
    if h_ab == h_cd:
        print("Yes")
    else:
        print("No")