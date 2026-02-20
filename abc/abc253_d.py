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

N, A, B = map(int,input().split())

c_A = N // A
c_B = N // B

AandB = math.lcm(A, B)
if N >= AandB:
    c_AandB = N // AandB
else:
    c_AandB = 0

sum_A = A * c_A * (c_A +1) // 2
sum_B = B * c_B * (c_B +1) // 2
sum_AandB = AandB * c_AandB * (c_AandB +1) // 2

res = sum_A + sum_B - sum_AandB
all = N * (N+1) // 2
print(all - res)

