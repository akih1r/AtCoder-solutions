import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
#N=int(input())
#A = [0] + list(map(int,input().split()))
#ls = [list(map(int, input().split())) for _ in range(N)]
#grid = [list(input()) for _ in range(N)]
#alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#N, A = map(int,input().split())
#X = list(map(int,input().split()))

N = int(input())
A = [0] + list(map(int,input().split()))
Q = int(input())

#L <= A[i]であるような最小のiをさがす
# iが奇数であればL_idx=i-1そうでなければ,L_idx=i
#R<= A[i]であるような最大のiwをさがす
# iが奇数であればR-A[i-1]を総和についか,あとにA[i-1]-A[L_idx]をついか
#そうでなければR_idx=i-1あとはおなじ



N = int(input())
A = [0] + list(map(int, input().split()))
Q = int(input())

S = [0] * (N + 1)
for i in range(2, N + 1):
    if i % 2 == 1:
        S[i] = S[i-1] + (A[i] - A[i-1])
    else:
        S[i] = S[i-1]


for _ in range(Q):
    L, R = map(int, input().split())
    
    idx_r = bisect.bisect_right(A, R) - 1
    if idx_r < 1:
        ans_r = 0
    elif idx_r % 2 == 0:
        ans_r = S[idx_r] + (R - A[idx_r])
    else:
        ans_r = S[idx_r]
        
    idx_l = bisect.bisect_right(A, L) - 1
    if idx_l < 1:
        ans_l = 0
    elif idx_l % 2 == 0:
        ans_l = S[idx_l] + (L - A[idx_l])
    else:
        ans_l = S[idx_l]
        
    print(ans_r - ans_l)