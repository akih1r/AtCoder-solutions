N, M, K = map(int,input().split())
dist = [[float("inf")]*(M+1) for i in range(M+1)]
for i in range(K):
    u,v,w = map(int,input().split())
    dist[u][v] = w
    dist[v][u] = w

for i in range(1,M+1):
    for j in range(1,M+1):
        if i == j:
            dist[i][j] = 0

for k in range(1,M+1):
    for i in range(1,M+1):
        for j in range(1,M+1):
            dist[i][j] = min(dist[i][k]+dist[k][j], dist[i][j])

ans = 0
for i in range(N):
    s, t = map(int,input().split())
    ans += dist[s][t]
print(ans) 