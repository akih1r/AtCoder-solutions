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

N, K = map(int,input().split())
path = defaultdict(int)
A = list(map(int,input().split()))
for i in range(N):
    path[i+1] = A[i]

visited1 = {}
cnt = 0
def f1(now, step):
    if now in visited1:
        return now, step
    visited1[now] = step
    return f1(path[now], step+1)

start, step = f1(1, 0)

visited2 = set()
def f2(now, lst):
    if now in visited2:
        return lst
    visited2.add(now)
    return f2(path[now], lst + [now])
    

l = f2(start, [])
r = (K - step) % len(l)

print(l[r])


            
    
    
    