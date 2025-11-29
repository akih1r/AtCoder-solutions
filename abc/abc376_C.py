import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations
sys.setrecursionlimit(10**7)



N = int(input())
A = sorted(list(map(int,input().split())))
B = sorted(list(map(int,input().split())))

def is_ok(x):
        bb = B + [x]
        bb.sort()
        if any(bb[k] < A[k] for k in range(N)):
                return False
        else:
            return True
        
    
ng, ok = -1, (1 << 30) +1

if not is_ok(ok):
    print(-1)
    exit()

def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok
print(meguru_bisect(ng, ok))
        
                
        
        
