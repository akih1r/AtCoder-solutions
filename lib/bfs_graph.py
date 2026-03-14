from collections import deque, defaultdict

N, M = map(int,input().split())
G = defaultdict(list)
for i in range(M):
    u, v = map(int,input().split())
    G[u].append(v)
    G[v].append(u)


def bfs(start, v_scale):
    que = deque([start])
    dist = [-1]*(v_scale+1)
    dist[start] = 0
    while que:
        now = que.popleft()
        for nxt in G[now]:
            if dist[nxt] == -1:
                dist[nxt] = dist[now]+1
                que.append(nxt)
    return dist



