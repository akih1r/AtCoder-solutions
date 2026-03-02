import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
#N=int(input())
N, M= map(int,input().split())
#A = list(map(int,input().split()))
#ls = [list(map(int, input().split())) for _ in range(N)]
#grid = [list(input()) for _ in range(N)]
#alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#N, A = map(int,input().split())
#X = list(map(int,input().split()))

N = int(input())
X = []
Y = []
for i in range(N):
    x, y = map(int,input().split())
    X.append(x);Y.append(y)

dp = [0]*(N+1)

for i in range(1,N+1):
    x, y = X[i-1], Y[i-1]
    if y == 0:
        dp[i] = dp[i-1] + 1
    elif y == x + 1:
        dp[i] = dp[i-1]
    else:
        prev_index = max(0, i - x - 1)
        num_agree = dp[i-1] - dp[prev_index]
        
        if num_agree >= y:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = dp[i-1]


print(dp[N])    

            
        