import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations
sys.setrecursionlimit(10**7)



N, R = map(int, input().split())
L = list(map(int, input().split()))

#全部１のとき操作不要
if 0 not in L:
    print(0)
    exit()

#一番左の開いてるドア
for i, v in enumerate(L):
    if v == 0:
        l = i
        break
l = min(R,l)


for i in range(N-1, -1,-1):
    if L[i] == 0:
        r = i
        break
r = max(R-1, r)
#条件付きで累積和リスト
S = [0] * (N + 1)
for i in range(l, r+1):
    S[i] = S[i-1] + (1 if L[i] == 0 else 2)
del S[0]

print(max(S))
