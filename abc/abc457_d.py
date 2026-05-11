import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math

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
#
#=========================================================

N, K = map(int,input().split())
A = list(map(int,input().split()))



#めぐる式二分探索
def is_ok(mid):
    used = 0
    for i in range(N):
        if A[i] < mid:
            used += ((mid-A[i]+(i+1))-1) // (i+1)
        if used > K:
            return False

    
    return True
    


def meguru_bisect(ng, ok):
    
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

ok = min(A)
ng = 2 * 10**18+1
mi = meguru_bisect(ng, ok)
print(mi)
