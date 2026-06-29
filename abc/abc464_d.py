import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
from sortedcontainers import SortedSet, SortedList, SortedDict

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
#lst = sorted(lst, key=lambda x:x[1], reverse = True)
#=========================================================


T = int(input())

for _ in range(T):
    N = int(input())
    S = input()
    X = list(map(int,input().split()))
    Y = list(map(int,input().split()))
    
    INF = 10**18
    dp = [{"S": -INF, "R": -INF} for _ in range(N)]
    
    if S[0] == "S":
        dp[0]["S"] = 0
        dp[0]["R"] = -X[0]
    else:
        dp[0]["S"] = -X[0]
        dp[0]["R"] = 0
    
    for i in range(1, N):
        cost_S = 0 if S[i] == "S" else -X[i]
        cost_R = 0 if S[i] == "R" else -X[i]
        
        if dp[i-1]["S"] > dp[i-1]["R"]:
            dp[i]["R"] = dp[i-1]["S"] + cost_R
        else:
            dp[i]["R"] = dp[i-1]["R"] + cost_R

        if dp[i-1]["R"] + Y[i-1] > dp[i-1]["S"]:
            dp[i]["S"] = dp[i-1]["R"] + Y[i-1] + cost_S
        else:
            dp[i]["S"] = dp[i-1]["S"] + cost_S

    print(max(dp[N-1]["S"], dp[N-1]["R"]))