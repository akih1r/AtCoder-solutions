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
acc = list(accumulate(A))
#累積和の累積マックス
max_A = []
max_ = float('-inf')
for i in range(N):
    max_ = max(acc[i],max_)
    max_A.append(max_)
now = 0
ans = 0
candidate = 0
for i in range(N):
    
    candidate = now + max_A[i]
    ans = max(candidate, ans)
    now += acc[i]
print(ans)