import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
#N=int(input())
#N, T = map(int,input().split())
#A = list(map(int,input().split()))
#ls = [list(map(int, input().split())) for _ in range(N)]
#grid = [list(input()) for _ in range(N)]
#alpha = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]

from collections import deque

N, Q = map(int,input().split())


A = list(map(int,input().split()))
acc = [0] + list(accumulate(A))

for i in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        x = q[1]-1
        A[x], A[x+1] = A[x+1], A[x]
        acc[x+1] = acc[x] + A[x]
        
        
        
    else:
        l,r = q[1]-1, q[2]-1
        print(acc[r+1]-acc[l])
  