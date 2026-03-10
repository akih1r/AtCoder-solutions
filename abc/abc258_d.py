import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
#N=int(input())
#N, M= map(int,input().split())
#A = [0] + list(map(int,input().split()))
#ls = [list(map(int, input().split())) for _ in range(N)]
#grid = [list(input()) for _ in range(N)]
#alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#N, A = map(int,input().split())
#X = list(map(int,input().split()))



N, X = map(int,input().split())
A = []
B = []
for i in range(N):
    a, b = map(int,input().split())
    A.append(a)
    B.append(b)


acc_AB = [a+b for a, b in zip(A,B)]
acc_AB = list(accumulate(acc_AB))
acc_minB = [0]*N
min_ = 10**10
for i in range(N):
    if B[i] < min_:
        min_ = B[i]
    acc_minB[i] = min_

cost = [0]*N

for i in range(N):
    clearnum = i+1
    needed_num = X - clearnum
    cost[i] = acc_minB[i]*needed_num + acc_AB[i]

print(min(cost))