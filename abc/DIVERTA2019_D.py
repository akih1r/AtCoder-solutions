import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


N = int(input())
yakusu = make_divisors(N)
ans = 0
for p in yakusu:
    mplus1 = N // p
    if not p < mplus1 -1 :
        continue
            
    if p * mplus1 == N:
        ans += (mplus1 - 1)
print(ans)
            
        
    
        


    

        
