import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
#N=int(input())
N, M, K= map(int,input().split())
#A = list(map(int,input().split()))
#B = list(map(int,input().split()))

#ls = [list(map(int, input().split())) for _ in range(N)]
#grid = [list(input()) for _ in range(N)]
#alpha = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]




MOD = 998244353

dp = [[0] * (K + 1) for _ in range(N + 1)]


dp[0][0] = 1

for i in range(N):
    for j in range(K + 1):
        if dp[i][j] == 0:
            continue
        
        # 次の項として 1 から M を追加する
        for add in range(1, M + 1):
            if j + add <= K:
                dp[i+1][j+add] += dp[i][j]
                dp[i+1][j+add] %= MOD
            else:
                break

#長さが N で、合計が K 「以下」 のものを全て足す
ans = sum(dp[N]) % MOD
print(ans)