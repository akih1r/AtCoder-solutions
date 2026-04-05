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

#一つの要素に操作をくわえてその後全体の最大最小をみる典型？

hp = []
N, K = map(int,input().split())
A = []
B = []
for i in range(N):
    a, b = map(int,input().split())
    A.append(a)
    B.append(b)
    hp.append((a, i))
heapq.heapify(hp)
time = 0
while K > 0:
    min_, idx = heapq.heappop(hp)
    time += min_
    K -= 1
    heapq.heappush(hp,(min_ + B[idx], idx))

print(time)
    
    


    

