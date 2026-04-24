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



#頂点倍加？BFS
#dist[i][j][縦に移動できるか横に移動できるか]=距離
#縦は０横は１とする


from collections import deque

que = deque()
H, W = map(int, input().split())
grid = [input() for _ in range(H)]

for i in range(H):
    for j in range(W):
        if grid[i][j] == "S":
            sy, sx = i, j
        elif grid[i][j] == "G":
            gy, gx = i, j



dist = [[[-1]*2 for j in range(W)] for _ in range(H)]


tate = [(1,0), (-1,0)]
yoko = [(0,-1), (0,1)]
dist[sy][sx][0] = 0
dist[sy][sx][1] = 0
que.append((sy, sx, 0))
que.append((sy, sx, 1))
ans = -1
while que:
    y, x, d = que.popleft()

    if (y, x) == (gy, gx):
        pass
    
    if d == 0:
        shift = tate
    else:
        shift = yoko
    
    

    for dy, dx in shift:
        ny, nx = y + dy, x + dx
        next_d = (d+1) % 2

        if 0 <= ny < H and 0 <= nx < W and grid[ny][nx] != '#' and dist[ny][nx][next_d] == -1:
            dist[ny][nx][next_d] = dist[y][x][d] + 1   # ← ここが dist の更新
            que.append((ny, nx, next_d))

res = []
if dist[gy][gx][0] != -1: res.append(dist[gy][gx][0])
if dist[gy][gx][1] != -1: res.append(dist[gy][gx][1])

if res:
    print(min(res))
else:
    print(-1)