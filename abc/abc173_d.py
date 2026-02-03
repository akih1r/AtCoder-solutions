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

N = int(input())
A = sorted(list(map(int,input().split())), reverse=True)


q = deque()
q.append(A[0])

for i in range(1, N):
    q.append(A[i])
    q.append(A[i])


ans = 0
for _ in range(N-1):
    ans += q.popleft()

print(ans)
    
    
  