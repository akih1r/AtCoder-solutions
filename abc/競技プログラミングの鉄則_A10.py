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


cnt = defaultdict(int)
N, K = map(int,input().split())
A = list(map(int,input().split()))

r = 0
now = 0
ans = 0
for l in range(N):
    while r < N and ((cnt[A[r]] > 0) or (now + 1 <= K)):
        if cnt[A[r]] == 0:
            now += 1
        cnt[A[r]] += 1
        r += 1
        

    
    ans = max(ans, r-l)
    
    if l == r:
        r += 1
    else:
        cnt[A[l]] -= 1
        if cnt[A[l]] == 0:
            now -= 1
    
    
    