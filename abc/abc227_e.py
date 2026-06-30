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
from collections import defaultdict, deque

input = sys.stdin.readline

N, M, K = map(int, input().split())
G = defaultdict(list)
for _ in range(M):
    u, v, a = map(int, input().split())
    G[u].append((v, a))
    G[v].append((u, a))
S = set()
if K > 0:
    S = set(map(int, input().split()))

visited = [[-1] * 2 for _ in range(N + 1)]
queue = deque([(1, 0)])
visited[1][0] = 0
while queue:
    now, flag = queue.popleft()
    if now in S:
        nflag = flag ^ 1
        if visited[now][nflag] == -1:
            visited[now][nflag] = visited[now][flag]
            queue.appendleft((now, nflag))
    for nex, a in G[now]:
        if (flag == 0 and a == 1) or (flag == 1 and a == 0):
            if visited[nex][flag] != -1:
                continue
            visited[nex][flag] = visited[now][flag] + 1
            queue.append((nex, flag))

ans = min(v for v in visited[N] if v != -1) if max(visited[N]) != -1 else -1
print(ans)