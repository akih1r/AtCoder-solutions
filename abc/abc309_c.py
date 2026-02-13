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

N, K = map(int,input().split())
event = []

for day in range(1,N+1):
    a, b = map(int,input().split())
    event.append((1, b))
    end_day = 1 + a
    event.append((end_day, -b))


heapq.heapify(event)

have = 0


while event:
    current_day = event[0][0]
    
    while event and event[0][0] == current_day:
        a, b = heapq.heappop(event)
        have += b
    if have <= K:
        print(current_day)
        break

    