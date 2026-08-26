import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate, groupby
sys.setrecursionlimit(10**7)
import math
from sortedcontainers import SortedSet, SortedList, SortedDict

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
# print("Yes" if () else "No")
#=========================================================

"""
1 何ごとの話にすると見やすい？なにだけ持てばいい？

2 それについて、何がわかれば答えになる？


3 何を捨ててよく、なぜそれで足りる？何が効く？何が禁止？


4 その情報をそう更新/判定/集計すれば実装できる？

"""

#白を固定していったら少ない量で全部網羅できるか
#Wをi = kとしたときmax(acc_B[k:])がほしいつまり区間max
#これは最大値の累積で行けそう（後ろからの）
#[l:r]

N, M = map(int,input().split())
B = list(map(int,input().split()))
W = list(map(int,input().split()))
B.sort(reverse=True)
W.sort(reverse=True)
acc_B = list(accumulate(B))
acc_W = list(accumulate(W))
acc_B_max = [float("-inf")]*N

max_ = float("-inf")
for i in range(N):
    max_ = max(acc_B[N-i-1], max_)
    acc_B_max[N-i-1] = max_

ans = max(0, acc_B_max[0])
for j in range(min(M,N)):
    sum_w = acc_W[j]
    res = sum_w + acc_B_max[j]
    ans = max(res, ans)
print(ans)
    
    