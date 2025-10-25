import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations
sys.setrecursionlimit(10**7)


N, K = map(int,input().split())
P = list(map(int,input().split()))

# 初期化
hq = []
for i in range(K):
    hq.append(P[i])
heapq.heapify(hq)

mi = hq[0]
print(mi)

for i in range(K, N):
    x = P[i]
    if x > mi:
        # ヒープの最小要素を x で置き換える
        heapq.heapreplace(hq, x)
        mi = hq[0]
    # x <= mi のときはヒープに何も入れないし、miも変わらない
    print(mi)


    
