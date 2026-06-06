#grid DFS
H, W = map(int, input().split())
grid = [input() for _ in range(H)]

for i in range(H):
    for j in range(W):
        if grid[i][j] == "S":
            sy, sx = i, j
        elif grid[i][j] == "G":
            gy, gx = i, j

shift = [(1,0), (-1,0), (0,-1), (0,1)]
visited = [[False]*W for _ in range(H)]
stack = [(sy, sx)]

while stack:
    y, x = stack.pop()
    if visited[y][x]:
        continue
    visited[y][x] = True
    for dy, dx in shift:
        ny, nx = y + dy, x + dx
        if 0 <= ny < H and 0 <= nx < W and grid[ny][nx] != '#' and not visited[ny][nx]:
            stack.append((ny, nx))