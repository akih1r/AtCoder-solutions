import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations
sys.setrecursionlimit(10**7)

S = list(map(int,list(input())))
N = len(S)

s = []
for i in range(0,N-1):
    if int(S[i]) + 1 == int(S[i+1]):
        s.append((i,i+1))


cnt = len(s)
for l, r in s:
    while True:
        if l-1 < 0 or r+1 > N-1:
            break
        if S[l-1] == S[l] and S[r+1] == S[r]:
            l -= 1
            r += 1
            cnt += 1
        else:
            break


print(cnt)
