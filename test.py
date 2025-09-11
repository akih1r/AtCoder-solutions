import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations
sys.setrecursionlimit(10**7)


N = int(input())
A = list(map(int,input().split()))

d = defaultdict(list)
#木を作る
for i in range(0,N):
    d[A[i]].append(2*(i+1))
    d[A[i]].append(2*(i+1) + 1)
    d[2*(i+1)].append(A[i])
    d[2*(i+1)+1].append(A[i])

#BFSで１から各々までの距離を記録しておく

stack = deque()
dist = [-1]*(2*N+2)
stack.append(1)
dist[1] = 0
while stack:
    now = stack.popleft()
    for child in d[now]:
        if dist[child] != -1:
            continue
        stack.append(child)
        dist[child] = dist[now] + 1


for k in range(1, 2*N+2):
    print(dist[k])     
    
        





