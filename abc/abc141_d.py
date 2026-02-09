import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
#N=int(input())
#N, K= map(int,input().split())
#D = list(map(int,input().split()))
#B = list(map(int,input().split()))

#ls = [list(map(int, input().split())) for _ in range(N)]
#grid = [list(input()) for _ in range(N)]
#alpha = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]


import heapq

N, M = map(int, input().split())
A = list(map(int, input().split()))

que = [-x for x in A]
heapq.heapify(que)

#M回割引をつかう。毎回最大値を割引する。
for _ in range(M):
    t = heapq.heappop(que)
    
    heapq.heappush(que, -((-t) // 2))

print(-sum(que))