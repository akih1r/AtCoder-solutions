#BFS
from collections import deque

que = deque()
H, W = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
grid = [input() for _ in range(H)]

sy -= 1; sx -= 1
gy -= 1; gx -= 1

dist = [[-1]*W for _ in range(H)]

shift = [(1,0), (-1,0), (0,-1), (0,1)]  # 上下左右
que.append((sy, sx))
dist[sy][sx] = 0

while que:
    y, x = que.popleft()

    if (y, x) == (gy, gx):
        break

    for dy, dx in shift:
        ny, nx = y + dy, x + dx

        if 0 <= ny < H and 0 <= nx < W and grid[ny][nx] != '#' and dist[ny][nx] == -1:
            dist[ny][nx] = dist[y][x] + 1   # ← ここが dist の更新
            que.append((ny, nx))

#print(dist[gy][gx])
