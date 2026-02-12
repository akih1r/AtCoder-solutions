import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
#N=int(input())
#N, K= map(int,input().split())
#D = list(map(int,input().split()))
#B = list(map(int,input().split()))

#ls = [list(map(int, input().split())) for _ in range(N)]
#grid = [list(input()) for _ in range(N)]
alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


N = int(input())
S = list(input())
Q = int(input())

d = defaultdict(str)
for char in alpha:
    d[char] = char

for i in range(Q):
    c, di = map(input().split())
    
    for w in alpha:#ここが肝
        if d[w] == c:
            d[w] = di


for i, char in enumerate(S):
    after = d[char]
    S[i] = after

print("".join(S))