import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
#N = int(input())
#A = list(map(int,input().split()))
A, B, C, X, Y = map(int,input().split())
#ABピザの数を決め打ち

ans = float('inf')
for p_c in range(2 * 10**5 + 1):
    all_yen = C * p_c
    p_a = X - (p_c // 2)
    p_b = Y - (p_c // 2)
    if p_a > 0:
        all_yen += p_a * A
    if p_b > 0:
        all_yen += p_b * B
    
    ans = min(ans, all_yen)
    
print(ans)
