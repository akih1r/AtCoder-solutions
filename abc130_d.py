import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations
sys.setrecursionlimit(10**7)


import bisect

N, K = map(int, input().split())
A = list(map(int, input().split()))

def make_cum(A, N):
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    return S

acc = make_cum(A, N)

ans = 0

for l in range(N):
    target = acc[l] + K
    
    # acc の l+1 番目以降から探す必要があります (lo=l+1)
    # bisect_right - bisect_left で「個数」が求まります
    r1 = bisect.bisect_left(acc, target, lo=l+1)
    r2 = bisect.bisect_right(acc, target, lo=l+1)
    
    ans += (r2 - r1)  # r1からr2の間にある個数を足す

print(ans)


        
    




    