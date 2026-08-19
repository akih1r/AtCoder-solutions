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
AをBに一致させる最小操作
差ととる

2 それについて、何がわかれば答えになる？


3 何を捨ててよく、なぜそれで足りる？何が効く？何が禁止？


4 その情報をそう更新/判定/集計すれば実装できる？

"""
N = int(input())
A = list(map(int,input().split()))

minus_num = 0
abs_a = []
for i in range(N):
    if A[i] < 0:
        minus_num += 1
    abs_a.append(abs(A[i]))

min_abs = float("inf")
min_idx = -1
for i in range(N):
    if abs(A[i]) < min_abs:
         min_abs = abs(A[i])
         min_idx = i
    

if minus_num % 2 == 0:
    ans = sum(abs(A[i]) for i in range(N))
else:
    if A[min_idx] < 0:
        ans = sum(abs(A[i]) for i in range(N) if i != min_idx) + A[min_idx]   # そのまま
    else:
        ans = sum(abs(A[i]) for i in range(N) if i != min_idx) - A[min_idx]   # 反転
print(ans)
    
    