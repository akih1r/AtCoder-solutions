import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
#N=int(input())
#N, M, P = map(int,input().split())
#A = list(map(int,input().split()))
#B = sorted(list(map(int,input().split())))

#ls = [list(map(int, input().split())) for _ in range(N)]
#grid = [list(input()) for _ in range(N)]
#alpha = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]


import sys
import heapq

# 入力を受け取る
# N: 参加人数, K: K番目の若さを知りたい
N, K = map(int, input().split())
X = list(map(int, input().split()))


# ここには常に「現時点で最も若いK人」を入れる
#トップKをつねに残しておく
pq = []


for i in range(N):
    age_rank = X[i]
    
    heapq.heappush(pq, -age_rank)
    
    if len(pq) > K:
        heapq.heappop(pq)
    
    
    if i >= K - 1:
        print(-pq[0])