import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
from sortedcontainers import SortedSet, SortedList, SortedDict

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
#lst = sorted(lst, key=lambda x:x[1], reverse = True)
#=========================================================

"""
ABC408
1. 目的
高橋君が食べることのできるお菓子の個数を求める

2. それに関わる特徴、性質は？
当たりの何個かもっており、それを消費して先頭のお菓子をたべる
最初前からk個とり当たりがa個ある


3. 目的が達成するためにその性質をどう用いたら良いか？


4. 具体的にどう実装する？

"""


N = int(input())
S = input()

num_o = [0]
for i in range(len(S)):
    if S[i] == "o":
        num_o.append(num_o[-1] + 1)
    else:
        num_o.append(num_o[-1])
num_o = num_o[1:]


num_x = [0]
for i in range(len(S)):
    if S[i] == "x":
        num_x.append(num_x[-1] + 1)
    else:
        num_x.append(num_x[-1])
num_x = num_x[1:]


for k in range(N):
    eat = k+1
    head = k+1
    has_o = num_o[k]
    has_x = num_x[k]
    # 先頭からみてhas_o個目のxは何個目
    # has_o+has_x個になじめてなるxの場所
    idx = bisect.bisect_left(num_x, has_o+has_x)
    if idx > N-1:
        print(N)
        continue
    print(idx+1)
