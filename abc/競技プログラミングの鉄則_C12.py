import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math


          
N, M, K = map(int,input().split())
A, B = [], []
for i in range(M):
    a, b = map(int,input().split())
    A.append(a)
    B.append(b)


def score(l,r):
    cnt = 0
    for i in range(M):
        if l <= A[i] and B[i] <= r:
            cnt += 1
    return cnt

INF = 10**9
#dp[何章作ったか][何ページ目まで書いたか] = ｓの時点での最大スコア
dp = [[-INF] * (N + 1) for _ in range(K + 1)]

dp[0][0] = 0

#何章目
for i in range(1,K+1):
    #i章目(k,j]の区間を見る
    for j in range(1, N+1):
        for k in range(j):
            
            if dp[i-1][k] == -INF:
                continue
            
            #(k,j]の区間のスコアを取得
            #k+1がi章の一番最初のページでkがi-1章の最後のページ
            cur_score = score(k+1, j)
            new_score = dp[i-1][k] + cur_score
            if new_score > dp[i][j]:
                dp[i][j] = new_score

print(dp[K][N])

    
        


    

        
