import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
#N=int(input())
#N, K= map(int,input().split())
#D = list(map(int,input().split()))
#B = list(map(int,input().split()))

#ls = [list(map(int, input().split())) for _ in range(N)]
#grid = [list(input()) for _ in range(N)]
#alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


import sys, bisect

line1 = sys.stdin.readline().split()
if not line1: exit() 
N, M, D = map(int, line1)

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A.sort()

ans = -1

for b in B:
    idx = bisect.bisect_right(A, b + D)
    
    target_idx = idx - 1

    if target_idx >= 0:
        a = A[target_idx]
        if a >= b - D:
            ans = max(ans, a + b)

print(ans)