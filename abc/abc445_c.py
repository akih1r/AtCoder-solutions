import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
N=int(input())
#N, M= map(int,input().split())

A = [0] + list(map(int,input().split()))

#ls = [list(map(int, input().split())) for _ in range(N)]
#grid = [list(input()) for _ in range(N)]
#alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
ans = [0]*(N+1)

for i in range(N, 0, -1):
    if i == A[i]:
        ans[i] = i
    else:
        ans[i] = ans[A[i]]

for i in range(N):
    print(ans[i+1], end = " ")
        
        