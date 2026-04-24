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
#=========================================================import heapq


import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math

#=======================================================
# (スニペット部分は省略せずにそのまま残しています)
#=========================================================

X, Y, Z, K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

A.sort(reverse = True)
B.sort(reverse = True)
C.sort(reverse = True)

sum_ = A[0] + B[0] + C[0]
cur_idx = (0,0,0)

hp = []
heapq.heappush(hp, (-sum_, cur_idx))

visited = set()
visited.add(cur_idx)

cnt = 0
while cnt < K:
    sum_, cur_idx = heapq.heappop(hp)
    sum_ *= -1
    print(sum_)
    cnt += 1
    
    a_idx = cur_idx[0]
    b_idx = cur_idx[1]
    c_idx = cur_idx[2]

    for i in range(3):
        if i == 0 and a_idx+1 < X:
            nex_sum = sum_ - A[a_idx] + A[a_idx+1]
            nex_idx = (a_idx+1, b_idx, c_idx)
            if nex_idx not in visited:
                visited.add(nex_idx)
                heapq.heappush(hp, (-nex_sum, nex_idx))
        
        elif i == 1 and b_idx+1 < Y:
            nex_sum = sum_ - B[b_idx] + B[b_idx+1]
            nex_idx = (a_idx, b_idx+1, c_idx)
            if nex_idx not in visited:
                visited.add(nex_idx)
                heapq.heappush(hp, (-nex_sum, nex_idx))
        
        elif i == 2 and c_idx+1 < Z:
            nex_sum = sum_ - C[c_idx] + C[c_idx+1]
            nex_idx = (a_idx, b_idx, c_idx+1)
            if nex_idx not in visited:
                visited.add(nex_idx)
                heapq.heappush(hp, (-nex_sum, nex_idx))