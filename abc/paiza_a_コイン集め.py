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
#=========================================================import heapq




H, W, K = map(int, input().split())

grid = [list(map(int,input().split())) for _ in range(H)]


shift = [(1,0), (-1,0), (0,-1), (0,1)]
ans = -1
def dfs(sy, sx):
    global ans
    stack = [(sy, sx, 0, grid[sy][sx], 0)]
    visited = set()
    

    while stack:
        y, x, cnt, S, flag = stack.pop()
        
        if flag == 1:
            visited.remove((y,x))
            continue
            
        
        else:
            if cnt == K:
                ans = max(S, ans)
                continue
            
            stack.append((y, x, cnt +1, grid[y][x], 1))
            visited.add((y, x))

            for dy, dx in shift:
                ny, nx = y + dy, x + dx

                if 0 <= ny < H and 0 <= nx < W and (ny, nx) not in visited:
                    stack.append((ny, nx, cnt +1, S+grid[ny][nx], 0))
                
for i in range(H):
    for j in range(W):
        dfs(i, j)
print(ans)