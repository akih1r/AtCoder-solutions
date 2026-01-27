import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
#SN, M = map(int,input().split())
#S = list(input())
#A = list(map(int,input().split()))
#A, B, C, X, Y = map(int,input().split())

d1= defaultdict(int)
d2 = defaultdict(int)
N = int(input())
v = list(map(int,input().split()))
for i in range(0,N,2):
    d1[v[i]] += 1

for i in range(1,N,2):
    d2[v[i]] += 1

lst1 = [(k, v) for k, v in d1.items()]
lst2 = [(k, v) for k, v in d2.items()]
lst1.sort(key = lambda x: x[1], reverse = True)
lst2.sort(key = lambda x: x[1], reverse = True)
M = min(len(lst2), len(lst1))

lst1.append((-1,-1))
lst2.append((-1,-1))
num1 = lst1[0][0]
num2 = lst2[0][0]

if num1 == num2:
  if lst1[1][1] >= lst2[1][1]:
    num1 = lst1[1][0]
  else:
    num2 = lst2[1][0]
  
            

    
ans = 0
for i in range(0,N,2):
    if v[i] != num1:
        ans += 1

for i in range(1,N,2):
    if v[i] != num2:
        ans += 1

print(ans)


        
    