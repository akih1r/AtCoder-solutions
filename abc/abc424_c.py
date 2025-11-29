from collections import defaultdict
import sys
sys.setrecursionlimit(10**7) 

d = defaultdict(list)
N = int(input())
visited = set()
start = []

for i in range(N):
    a, b = map(int, input().split())
    if a != 0:
        d[a].append(i+1)
    if b != 0:
        d[b].append(i+1)
    if a == 0 and b == 0:
        start.append(i+1)

def dfs(now):
    visited.add(now)
    for j in d[now]:
        if j not in visited:
            dfs(j)

#多地点DFS
for s in start:
        dfs(s)

print(len(visited))