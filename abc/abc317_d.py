import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
#N=int(input())
#A =list(map(int,input().split()))
#ls = [list(map(int, input().split())) for _ in range(N)]
#grid = [list(input()) for _ in range(N)]
#alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#N, A = map(int,input().split())
#X = list(map(int,input().split()))



N = int(input())
X, Y, Z = [], [], []
for i in range(N):
    x, y, z = map(int,input().split())
    X.append(x);Y.append(y);Z.append(z)
X = [0] + X
Y = [0] + Y
Z = [0] + Z
num_Z = sum(Z)
dp = [[float("inf")]*(num_Z+1) for i in range(N+1)]
dp[0][0] = 0

for i in range(0,N):
    for j in range(0,num_Z+1):
        if dp[i][j] == float("inf"):
            continue
        
        if X[i+1]>=Y[i+1]:#Xの方が大きいとき鞍替えの必要はない
            dp[i+1][j+Z[i+1]] = min(dp[i][j], dp[i+1][j+Z[i+1]])
            continue
        
        #鞍替えさせない
        dp[i+1][j] = min(dp[i][j],dp[i+1][j])
        
        #鞍替えさせる
        add = ((X[i+1]+Y[i+1]) // 2) +1 -X[i+1]
        dp[i+1][j+Z[i+1]] = min(dp[i][j] + add, dp[i+1][j+Z[i+1]])

#求めるのはdp[N][j >= num_Z//2]の最小

lst = dp[N]
ans = min(lst[(num_Z//2)+1:])
print(ans)
    