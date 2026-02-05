import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
#N=int(input())
N, M, P = map(int,input().split())
A = list(map(int,input().split()))
B = sorted(list(map(int,input().split())))

#ls = [list(map(int, input().split())) for _ in range(N)]
#grid = [list(input()) for _ in range(N)]
#alpha = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]


accb = [0] + list(accumulate(B))
ans = 0
for i in range(N):
    idx = bisect.bisect_left(B, P-A[i])
    sum_left = ((M-1) - idx +1) * P
    sum_right = idx * A[i] + (accb[idx]-accb[0])
    ans += sum_left + sum_right

print(ans)
