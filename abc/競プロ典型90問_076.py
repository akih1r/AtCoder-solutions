import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
#N=int(input())
#A = [0] + list(map(int,input().split()))
#ls = [list(map(int, input().split())) for _ in range(N)]
#grid = [list(input()) for _ in range(N)]
#alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#N, A = map(int,input().split())
#X = list(map(int,input().split()))



N = int(input())
A = list(map(int,input().split()))
acc = A+A
acc = list(accumulate(acc))
K = sum(A)//10

#めぐる式二分探索
def is_ok(mid):
    if l-1 < 0:
        S =  acc[mid]
    else:
        S = acc[mid] - acc[l-1]
    if S < K:
        return False
    if S >= K:
        return True
        
    


def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok



for l in range(0,N):
    idx = meguru_bisect(l-1, 2*N)
    if l-1 < 0:
        S =  acc[idx]
    else:
        S = acc[idx] - acc[l-1]
    if S == K:
        print("Yes")
        exit()
print("No")
    
    