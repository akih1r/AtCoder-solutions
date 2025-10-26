import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations
sys.setrecursionlimit(10**7)

N = int(input())
A = list(map(int,input().split()))
dic = Counter(A)


num = sum(dic.values())
cnt = 0

for k, v in dic.items():
    if dic[k] >= 2:
        b = (dic[k] * (dic[k] -1)) // 2
        t = num - v
        cnt += b * t
        
    

print(cnt)