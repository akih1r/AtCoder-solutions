import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
#N=int(input())
#N, K= map(int,input().split())
#D = list(map(int,input().split()))
#B = list(map(int,input().split()))

#ls = [list(map(int, input().split())) for _ in range(N)]
#grid = [list(input()) for _ in range(N)]
#alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


N = int(input())
A = [0] + list(map(int,input().split()))
B = [0] + list(map(int,input().split()))

dp = [0]*(N+1)
for i in range(2,N+1):
    cost1 = dp[i-1] + A[i-1]
    if i-2 >= 1:
        cost2 = dp[i-2] + B[i-2]
        dp[i] = min(cost1, cost2)
    else:
        dp[i] = cost1

ans = []
pos = N
while True:
    ans.append(pos)
    if pos == 1:
        break
    
    if dp[pos] == dp[pos-1] + A[pos-1]:
        pos = pos -1
    
    elif dp[pos] == dp[pos-2] + B[pos-2]:
        pos = pos -2

ans.reverse()

print(len(ans))
print(*ans)