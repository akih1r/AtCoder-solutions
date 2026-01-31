import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math


T = int(input())

for i in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    dp = [0]*N
    dp[0] = A[0]
    for i in range(1,N):
        #i番目をペアにするか単独にするか
        pattern1 = dp[i-1] + A[i]
        
        if i >= 2:
            pattern2 = dp[i-2] + max(A[i], A[i-1])
        else:
            pattern2 = max(A[i], A[i-1])
        
        dp[i] = min(pattern1, pattern2)
    
    print(dp[N-1])
        
        


    

        
