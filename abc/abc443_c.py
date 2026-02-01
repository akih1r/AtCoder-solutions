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



def solve():
    N = int(input())
    R = list(map(int,input().split()))
    hp = []
    cnt = 0
    for i in range(N):
        hp.append((R[i], i))
    
    heapq.heapify(hp)
    while hp:
        val, idx = heapq.heappop(hp)
        goal = val + 1
        
        if idx + 1 < N and R[idx + 1] > goal:
            cnt += R[idx+1] - goal
            R[idx+1] = goal
            heapq.heappush(hp, (goal, idx+1))
        
        if idx - 1 >= 0 and R[idx - 1] > goal:
            cnt += R[idx-1] - goal
            R[idx-1] = goal
            heapq.heappush(hp, (goal, idx-1))
    print(cnt)
    

T = int(input())
for _ in range(T):
    solve()
        
