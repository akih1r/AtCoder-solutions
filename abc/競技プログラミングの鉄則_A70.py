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



from collections import deque

N, M = map(int, input().split())
A = list(map(int, input().split()))

# 初期状態をビット列（整数）に変換
start = 0
for i in range(N):
    if A[i] == 1:
        start |= (1 << i)

# 目標状態はすべてのビットが1（= 2^N - 1）
goal = (1 << N) - 1

# 操作もビットマスクとして保存
ops = []
for _ in range(M):
    x, y, z = map(int, input().split())
    # 0-indexedに変換
    x -= 1
    y -= 1
    z -= 1
    ops.append((1 << x) | (1 << y) | (1 << z))

# 各状態までの最小操作回数を管理（-1は未到達）
dist = [-1] * (1 << N)
dist[start] = 0

q = deque([start])

ans = -1

# 幅優先探索 (BFS)
while q:
    curr = q.popleft()
    
    # 目標状態に到達したら終了
    if curr == goal:
        ans = dist[curr]
        break
        
    # 各操作を試す
    for op in ops:
        # XOR演算(^)で状態を反転
        nxt = curr ^ op
        
        # まだ到達していない状態ならキューに追加
        if dist[nxt] == -1:
            dist[nxt] = dist[curr] + 1
            q.append(nxt)

print(ans)