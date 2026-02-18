import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
#N=int(input())
#N, M= map(int,input().split())

#A = [0] + list(map(int,input().split()))

#ls = [list(map(int, input().split())) for _ in range(N)]
#grid = [list(input()) for _ in range(N)]
#alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

N, S = map(int,input().split())

dp = [[0]* (S+1) for _ in range(N+1)]
dp[0][0] = 1
A = []
B = []
for i in range(N):
    a, b = map(int,input().split())
    A.append(a)
    B.append(b)
for i in range(N):
    for k in range(S + 1):
        if dp[i][k] > 0:
            if k + A[i] <= S:
                dp[i + 1][k + A[i]] += dp[i][k]
            if k + B[i] <= S:
                dp[i + 1][k + B[i]] += dp[i][k]

if dp[N][S] > 0:
    print("Yes")
else:
    print("No")
    exit()


# 経路復元
res = []
current_s = S

# N枚目から1枚目まで逆順に辿る
for i in range(N - 1, -1, -1):
    if current_s - A[i] >= 0 and dp[i][current_s - A[i]] > 0:
        res.append("H")
        current_s -= A[i]
    else:
        res.append("T")
        current_s -= B[i]



print("".join(reversed(res)))