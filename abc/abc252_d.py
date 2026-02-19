import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
#N=int(input())
#N, K= map(int,input().split())
#A = list(map(int,input().split()))
#ls = [list(map(int, input().split())) for _ in range(N)]
#grid = [list(input()) for _ in range(N)]
#alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math

N = int(input())
A = list(map(int,input().split()))
cnt = Counter(A)

# 全体の選び方 N C 3
ans = N * (N - 1) * (N - 2) // 6

for k, v in cnt.items():
    # 3つとも同じ値になる選び方 v C 3 を引く
    ans -= v * (v - 1) * (v - 2) // 6
    
    # 2つが同じ値で、1つが異なる値になる選び方 v C 2 * (N - v) を引く
    ans -= (v * (v - 1) // 2) * (N - v)

print(ans)