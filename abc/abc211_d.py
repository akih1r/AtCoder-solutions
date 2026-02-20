import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
#N=int(input())
#N, K= map(int,input().split())
#A = list(map(int,input().split()))
#ls = [list(map(int, input().split())) for _ in range(N)]
#grid = [list(input()) for _ in range(N)]
#alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math

#模範解答
import collections

# 入力
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    # 0-indexedに合わせる
    A -= 1
    B -= 1
    G[A].append(B)
    G[B].append(A)

MOD = 1000000007

# BFSの準備
que = collections.deque()
dp = [-1] * N
cnt = [0] * N


que.append(0)
dp[0] = 0
cnt[0] = 1

while que:
    u = que.popleft()
    for v in G[u]:
        if dp[v] == -1:
            que.append(v)
            dp[v] = dp[u] + 1
            cnt[v] = cnt[u]
        elif dp[v] == dp[u] + 1:
            cnt[v] += cnt[u]
            cnt[v] %= MOD

print(cnt[N-1])
