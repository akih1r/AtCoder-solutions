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
#=========================================================import heapq

#普通に総和をもとめる必要がある。最大化最小化でもないので
#主客転倒くさい

#A_iのときA_i+1からA_NまでのA_iとの差の総和が貢献した分
#絶対値場合分けA_iよりおおきいか小さいかの境界線を二分探索


N = int(input())
A = [0] + list(map(int,input().split()))
A.sort()

S = list(accumulate(A))
ans = 0
#iを固定
for i in range(1,N+1):
    idx = bisect.bisect_right(A,A[i]) -1
    sum1 = (idx)* A[i] - S[idx]
    sum2 = - (N-idx)*A[i] + (S[N] - S[idx])
    ans += sum1 + sum2
print(ans//2)


