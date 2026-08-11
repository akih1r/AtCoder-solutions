import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
from sortedcontainers import SortedSet, SortedList, SortedDict

#=======================================================
#
# N=int(input())
# A =list(map(int,input().split()))
# S = [0] + accmulate(A)
# ls = [list(map(int, input().split())) for _ in range(N)]
# grid = [list(input()) for _ in range(N)]
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
O(２^N)までいける全探索で行けそう
どう区間にわける？
区切り線でビット全探索してそれぞれの区間を愚直にもとめる？

2 それについて、何がわかれば答えになる？


3 何を捨ててよく、なぜそれで足りる？何が効く？何が禁止？


4 その情報をそう更新/判定/集計すれば実装できる？

"""
N = int(input())
A = list(map(int,input().split()))
#区切り線なのでN-1個のマスクがあればいい
ans = 10**9
for bit in range(1 << (N-1)):  # 1 << N は 2**N と同じ意味
        
        mask = []
        for i in range(N-1):
            if (bit >> i) & 1:
                mask.append(1)
            else:
                mask.append(0)
        
        #そのマスクについて
        or_ = 0
        res = []
        for i in range(N):
            if i == N-1:
                or_ |= A[i]
                res.append(or_)
                break
                
            or_ |= A[i]
            if mask[i] == 1:
                res.append(or_)
                or_ = 0
        
        
        xor_ = res[0]
        for r in res[1:]:
            xor_ ^= r
        ans = min(xor_, ans)
print(ans)
                