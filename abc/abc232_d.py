import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
#N=int(input())
#N, M= map(int,input().split())
#A = list(map(int,input().split()))
#ls = [list(map(int, input().split())) for _ in range(N)]
#grid = [list(input()) for _ in range(N)]
#alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#N, A = map(int,input().split())
#X = list(map(int,input().split()))



import sys


n, m = map(int, input().split())


c = [list(input()) for _ in range(n)]


f = [[0] * m for _ in range(n)]


if c[0][0] != '#':
    f[0][0] = 1

#配るDP
for i in range(n):
    for j in range(m):
        
        if c[i][j] == '#' or f[i][j] == 0:
            continue
        
        
        if i + 1 < n and c[i+1][j] != '#':
            
            if f[i][j] + 1 > f[i+1][j]:
                f[i+1][j] = f[i][j] + 1
        

        if j + 1 < m and c[i][j+1] != '#':
            if f[i][j] + 1 > f[i][j+1]:
                f[i][j+1] = f[i][j] + 1


ans = 0
for i in range(n):
    for j in range(m):
        if f[i][j] > ans:
            ans = f[i][j]

print(ans)