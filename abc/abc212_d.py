import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
#N=int(input())
#N, M= map(int,input().split())
#A = list(map(int,input().split()))
#ls = [list(map(int, input().split())) for _ in range(N)]
#grid = [list(input()) for _ in range(N)]
#alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#N, A = map(int,input().split())
#X = list(map(int,input().split()))

import heapq

Q = int(input())

offset = 0
que = []

for _ in range(Q):
    query = list(map(int, input().split()))
    T = query[0]
    
    if T == 1:
        X = query[1]
        heapq.heappush(que, X - offset)
    elif T == 2:
        X = query[1]
        offset += X
    else:
        ans = heapq.heappop(que) + offset
        print(ans)