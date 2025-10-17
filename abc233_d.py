import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations
sys.setrecursionlimit(10**7)

#ABC105-Dと同じ累積和典型問題
#条件を満たす区間和の式S[r] -S[l-1] = Kを変形し
#S[l-1] = S[r] - Kを満たすiがあると連想配列に記録とans++
N = int(input())
A = list(map(int,input().split()))

def make_cum(A,N):
    N = len(A)
    S = [0]*(N+1)
    S[0] = 0
    for i in range(0,N):
        S[i+1] = S[i] + A[i]
    return S

S = make_cum(A,N)
cnt = defaultdict(int)
ans = 0

for i in S:
    ans += cnt[i]
    cnt[i] += 1

print(ans)
    
    

