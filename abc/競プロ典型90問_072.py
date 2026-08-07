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

"""
1. 目的
鉄道路線が通るマスの数としてあり得る最大値（家を含めて）

2. それに関わる特徴、性質は？
制約が小さい
単純パスだから行きがけ帰りがけで

3. 目的が達成するためにその性質をどう用いたら良いか？
制約が小さいので全探索でいけそう

4. 具体的にどう実装する？
山以外のマスからスタート

"""

H, W = map(int, input().split())

grid = [input() for _ in range(H)]


shift = [(1,0), (-1,0), (0,-1), (0,1)]
ans = -1
def dfs(sy, sx):
    sy, sx = sy, sx
    global ans
    stack = [(sy, sx, 1, 0)]
    visited = set()
    

    while stack:
        y, x, k, flag = stack.pop()
        
        if flag == 1:#帰りがけ
            visited.remove((y,x))
            continue
            
        
        else:
            if (y, x) == (sy, sx) and k >= 3:
                ans = max(ans, k)
            
            stack.append((y, x, k , 1))
            visited.add((y, x))

            for dy, dx in shift:
                ny, nx = y + dy, x + dx
                if (ny, nx) == (sy, sx):         # 始点に戻った = 閉路成立
                    if k >= 3:
                        ans = max(ans, k)
                    continue

                if 0 <= ny < H and 0 <= nx < W and grid[ny][nx] != '#' and (ny, nx) not in visited:
                    stack.append((ny, nx, k +1, 0))
                
for i in range(H):
    for j in range(W):
        if grid[i][j] == ".":
            dfs(i, j)
print(ans)