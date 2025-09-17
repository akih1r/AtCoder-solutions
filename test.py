import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations
sys.setrecursionlimit(10**7)



S = list(map(int,list(input())))
cnt = 0
shift = 0
for _ in range(len(S)):
        S[-1] =  (S[-1] - shift) % 10
        shift += S[-1]
        cnt += S[-1]
        cnt += 1
        S.pop()
print(cnt)