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


#隣がダブっちゃいけないだけだから、DPでいける。そうじゃないならDFSのかえりがけ
N = int(input())
A = []
B = []
for i in range(N):
    a, b = map(int,input().split())
    A.append(a);B.append(b)
MOD = 998244353

dp = [{'A': 0, 'B': 0} for _ in range(N)]

dp[0]['A'] = 1
dp[0]['B'] = 1
for i in range(N-1):
    for j in ['A','B']:
        if dp[i][j] == 0:
            continue
        if j == "A":
            if A[i+1] != A[i]:
                dp[i+1]['A'] += dp[i][j]% MOD
            if B[i+1] != A[i]:
                dp[i+1]['B'] += dp[i][j]% MOD
        else:
            if A[i+1] != B[i]:
                dp[i+1]['A'] += dp[i][j]% MOD
            if B[i+1] != B[i]:
                dp[i+1]['B'] += dp[i][j]% MOD

print((dp[N-1]['A'] + dp[N-1]['B']) % MOD)