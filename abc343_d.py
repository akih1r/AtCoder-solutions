import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations
sys.setrecursionlimit(10**7)

N, T = map(int,input().split())
point = [0]*N

numb = defaultdict(int)
numb[0] = N

kinds = 1
for i in range(T):
    a, b = map(int, input().split())
    a -= 1
    before_mypoint = point[a]
    after_mypoint  = point[a] + b
    
    num_before = numb[before_mypoint]
    num_after = numb[after_mypoint]
    if before_mypoint == after_mypoint:
        print(kinds)
        continue
    if num_before >= 2 and num_after + 1 >= 2:
        kinds = kinds
    elif num_before >= 2 and num_after +1 < 2:
        kinds += 1
    elif num_before < 2 and num_after +1 >= 2:
        kinds -= 1
    else:
        kinds = kinds
    print(kinds)
    #更新
    point[a] += b
    numb[before_mypoint] -= 1
    numb[after_mypoint] += 1
        
    
    
    
    
