import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math

#=======================================================
#
#N=int(input())
#A =list(map(int,input().split()))
#S = [0] + accmulate(A)
#ls = [list(map(int, input().split())) for _ in range(N)]
#grid = [list(input()) for _ in range(N)]
#alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#N, M, T = map(int,input().split())
#G = defaultdict(list)
#for i in range(M):
#    u, v = map(int,input().split())
#    G[u].append(v)
#    G[v].append(u)
#
#=========================================================



#dp[i][pre] = i番目まで選び終わった後の最大値
N=int(input())
A =list(map(int,input().split()))
dp = [[-1] * 2 for i in range(N)]
dp[0][0] = 0
dp[0][1] = A[0]

if N == 1:
    print(A[0])
    exit()

for i in range(N-1):
    for b in [0,1]:
        if dp[i][b] == -1:
            continue
        
        if b == 0:
            #前回とってなくて今回とる
            dp[i+1][1] =  max(dp[i][b] + A[i+1], dp[i+1][1])
            #前回とってなくて今回とらない
            dp[i+1][0] = max(dp[i][b], dp[i+1][0])
        else:
            #前回とって今回とらない
            dp[i+1][0] = max(dp[i][b], dp[i+1][0])

print(max(dp[N-1]))
    
