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


N = int(input())
A = list(map(int,input().split()))
D = int(input())
#累積マックス
max_A = []
max_ = float('-inf')
for i in range(N):
    max_ = max(A[i],max_)
    max_A.append(max_)
#逆から累積マックス
max_rev = float('-inf')
max_A_rev = []
for j in range(N-1,-1,-1):
    max_rev = max(A[j],max_rev)
    max_A_rev.append(max_rev)
max_A_rev.reverse()
    

for i in range(D):
    l, r = map(int,input().split())
    l -= 1; r -= 1
    if l-1 < 0:
        l_max = -1
    else:
        l_max = max_A[l-1]
    if r+1 >= N:
        r_max = -1
    else:
        r_max = max_A_rev[r+1]
    print(max(r_max, l_max))
    