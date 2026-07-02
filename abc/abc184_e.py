import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
from sortedcontainers import SortedSet, SortedList, SortedDict

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
#lst = sorted(lst, key=lambda x:x[1], reverse = True)
#=========================================================

import sys
from collections import deque, defaultdict
input = sys.stdin.readline

H, W = map(int, input().split())
grid = [input().rstrip() for _ in range(H)]

spot = defaultdict(list)
for i in range(H):
    for j in range(W):
        c = grid[i][j]
        if c == "S":
            sy, sx = i, j
        elif c == "G":
            gy, gx = i, j
        elif c.islower():
            spot[c].append((i, j))

time = [[-1] * W for _ in range(H)]
que = deque([(sy, sx)])
shift = [(1, 0), (-1, 0), (0, -1), (0, 1)]
used = set()  

while que:
    y, x = que.popleft()
    if (y, x) == (gy, gx):
        break

    for dy, dx in shift:
        ny, nx = y + dy, x + dx
        if 0 <= ny < H and 0 <= nx < W and grid[ny][nx] != '#' and time[ny][nx] == -1:
            time[ny][nx] = time[y][x] + 1
            que.append((ny, nx))

    # テレポートでテレポートしうるすべてのマスをpush
    c = grid[y][x]
    if c.islower() and c not in used:
        used.add(c)
        for nexi, nexj in spot[c]:
            if time[nexi][nexj] == -1:
                time[nexi][nexj] = time[y][x] + 1
                que.append((nexi, nexj))

print(time[gy][gx])