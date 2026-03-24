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
N, K, Q = map(int,input().split())
A =list(map(int,input().split()))
S = [0] + list(accumulate(A))





#めぐる式二分探索
def is_ok(mid, num):
    if mid >= N:
        return True
    if S[mid+1] - S[num] > K:
        return True
    else:
        return False
    


def meguru_bisect(ng, ok, num):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid, num):
            ok = mid
        else:
            ng = mid
    return ok



def f(num):
    return meguru_bisect(num-1, N+1, num)

F = [0]*(N+1)
for i in range(1,N+1):
    res = f(i-1)
    if res >= N:
        F[i] = N
    else:
        F[i] = res + 1

acc_F = [0]+ list(accumulate(F[1:]))

for i in range(Q):
    L, R = map(int,input().split())
    ans = acc_F[R] - acc_F[L-1]
    print(ans)
    
    