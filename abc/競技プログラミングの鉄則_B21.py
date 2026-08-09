import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
from sortedcontainers import SortedSet, SortedList, SortedDict

#=======================================================
#
# N=int(input())
# A =list(map(int,input().split()))
# S = [0] + accmulate(A)
# ls = [list(map(int, input().split())) for _ in range(N)]
# grid = [list(input()) for _ in range(N)]
# alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
# N, M, T = map(int,input().split())
# G = defaultdict(list)
# for i in range(M):
#     u, v = map(int,input().split())
#     G[u].append(v)
#     G[v].append(u)
# lst = sorted(lst, key=lambda x:x[1], reverse = True)
#=========================================================

"""
1. 目的

2. それに関わる特徴、性質は？

3. 目的が達成するためにその性質をどう用いたら良いか？

4. 具体的にどう実装する？

"""
# 入力
N = int(input())
S = input()

# 動的計画法（初期状態）
dp = [ [ None ] * N for i in range(N) ]
for i in range(N):
	dp[i][i] = 1
for i in range(N-1):
	if S[i] == S[i+1]:
		dp[i][i+1] = 2
	else:
		dp[i][i+1] = 1

# 動的計画法（状態遷移）
for LEN in range(2,N):
	for l in range(N-LEN):
		r = l + LEN
		if S[l] == S[r]:
			dp[l][r] = max(dp[l][r-1], dp[l+1][r], dp[l+1][r-1]+2)
		else:
			dp[l][r] = max(dp[l][r-1], dp[l+1][r])

# 出力
print(dp[0][N-1])