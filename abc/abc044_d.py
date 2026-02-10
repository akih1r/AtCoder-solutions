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

N, A = map(int, input().split())
x = list(map(int, input().split()))

#DP
dp = [[[0]*(3000) for i in range(51)] for _ in range(51)]
dp[0][0][0] = 1
S = 3000
for i in range(0, N):
    for j in range(0,N):
        for k in range(0,S):
            if dp[i][j][k]:
                dp[i+1][j][k] += dp[i][j][k]
                if k + x[i] <= S:
                    dp[i+1][j+1][k+x[i]] += dp[i][j][k]

ans = 0
for j in range(1, N+1):
    target_sum = j * A
    if target_sum < S+1:
        ans += dp[N][j][target_sum]

print(ans)
            