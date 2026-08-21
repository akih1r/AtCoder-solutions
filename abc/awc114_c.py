import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate, groupby
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
Diがボーナスステージのどれかにはいるかどうかをみたい
二分探索で愚直にいけない？
2 それについて、何がわかれば答えになる？


3 何を捨ててよく、なぜそれで足りる？何が効く？何が禁止？


4 その情報をそう更新/判定/集計すれば実装できる？

"""
N, M = map(int,input().split())
events = []
for i in range(N):
    x, c = map(int,input().split())
    events.append((x,1,c))

for i in range(M):
    l, r = map(int,input().split())
    events.append((l,0))
    events.append((r,2))
events.sort()
coverd = 0
ans = 0
for e in events:
    if e[1] == 0:
        coverd += 1
    elif e[1] == 1:
        if coverd >0:
            ans += e[2]
    else:
        coverd -= 1
print(ans)
    