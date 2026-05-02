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


H, W =map(int,input().split())
grid = [list(input()) for _ in range(H)]

visited = set()
white = []
for i in range(H):
    for j in range(W):
        if grid[i][j] == ".":
            white.append((i,j))
shift = [(1,0), (-1,0), (0,-1), (0,1)]

ans = 0
for i, j in white:
    flag = True
    if (i,j) in visited:
        continue
    

    if i == 0 or i == H-1 or j == 0 or j == W-1:
        flag = False
    stack = [(i,j)]
    visited.add((i,j))
    while stack:
        hi, hj = stack.pop()
        for di, dj in shift:
            ni, nj = hi+di, hj+dj
            
            #まず範囲内か
            if 0 <= ni < H and 0 <= nj < W:
                if (ni, nj) in visited:
                    continue
                
                if grid[ni][nj] == '#':
                    continue
                if ni == 0 or ni == H-1 or nj == 0 or nj == W-1:#白かつ外枠この塊はだめになるのでFalse
                    flag = False
    
                visited.add((ni, nj))
                stack.append((ni, nj))
    
    if flag:
        ans += 1
print(ans)
        
        