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

N = int(input())
X, Y = map(int,input().split())
A, B = [], []
for i in range(N):
    a, b, = map(int,input().split())
    A.append(a)
    B.append(b)
A = [0] + A
B = [0] + B
dp = [[[float('inf')]*(Y+1) for _ in range(0,X+1)] for _ in range(N+1)]
#dp[i][たこやき][たいやき]　=　弁当最小個数
dp[0][0][0] = 0
for i in range(0,N):
    for tako in range(0,X+1):
        for tai in range(0,Y+1):
            if dp[i][tako][tai] == float('inf'):
                continue
            #えらばない
            dp[i+1][tako][tai] = min(dp[i][tako][tai], dp[i+1][tako][tai])
            
            #えらぶ
            new_tako = min(tako + A[i+1], X)
            new_tai = min(tai + B[i+1], Y) 
            dp[i+1][new_tako][new_tai] = min(dp[i][tako][tai]+1,  dp[i+1][new_tako][new_tai])
ans = float('inf')
for i in range(0, N+1):
    ans = min(dp[i][X][Y],ans)
if ans == float('inf'):
    print(-1)
    exit()
print(ans)

