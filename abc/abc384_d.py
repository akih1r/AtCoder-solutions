import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
from sortedcontainers import SortedSet, SortedList, SortedDict
input = sys.stdin.readline
#=======================================================
#
# N=int(input())
# A =list(map(int,input().split()))
# S = [0] + accmulate(A)
# ls = [list(map(int, input().split())) for _ in range(N)]
# grid = [list(input().rstrip()) for _ in range(N)]
# alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
# N, M, T = map(int,input().split())
# G = defaultdict(list)
# for i in range(M):
#     u, v = map(int,input().split())
#     G[u].append(v)
#     G[v].append(u)
# lst = sorted(lst, key=lambda x:x[1], reverse = True)
#=========================================================

"""
1 何ごとの話にすると見やすい？なにだけ持てばいい？
まずSをsum(A)でわるそのあまりがAの要素で作れるかを判定したい
連続部分和問題？つまり尺取りで行けそう
K＝Sとなるものはあるか
端と端の区間も欲しいのでA＋Aを尺取りさせる



2 それについて、何がわかれば答えになる？


3 何を捨ててよく、なぜそれで足りる？何が効く？何が禁止？


4 その情報をそう更新/判定/集計すれば実装できる？

"""
N, S = map(int,input().split())
A = list(map(int,input().split()))
K = S % sum(A)
A2 = A + A
#ちょうど区間がKとなる区間があるかを尺取り

if K == 0:
    print("Yes")
    exit()
r = 0
sum_ = 0
for l in range(2*N):
    
    if l > r:
        r = l
        sum_ = 0
    while r < 2*N and sum_ + A2[r] < K:
        sum_ += A2[r]
        r += 1
    if sum_ + A2[r] == K:
        print("Yes")
        exit()
    if l < r:
        sum_ -= A2[l]
print("No")