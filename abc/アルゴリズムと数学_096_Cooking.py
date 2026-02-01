import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
#N=int(input())
#N, T = map(int,input().split())
#A = list(map(int,input().split()))
#ls = [list(map(int, input().split())) for _ in range(N)]
#grid = [list(input()) for _ in range(N)]
#alpha = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]




        


import sys

# 入力
N = int(input())
T = list(map(int, input().split()))

S = sum(T)


dp = 1

# Numpy版の DP[...] |= DP[...] に相当
for t in T:
    # dp << t : 今作れる値をすべて t だけずらす（tを足す）
    # dp | ... : 元の状態と合成する（OR演算）
    #1000110だと1、2、6分間オーブンAが稼働するパターンがあり得るということ
    dp |= (dp << t)

# 【答え】
# S // 2 以下で、ビットが立っている（作れる）最大の値を探す
half = S // 2
for i in range(half, -1, -1):
    # iビット目が1かチェック（ (dp >> i) & 1 ）
    if (dp >> i) & 1:
        # 見つかった i が「片方の和の最大値」
        # もう片方は S - i なので、大きい方の値である S - i を出力
        print(S - i)
        break