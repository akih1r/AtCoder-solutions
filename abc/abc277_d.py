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



class UnionFind:
    def __init__(self,n):
        self.parents = [-1]*n
    def find(self,x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if -self.parents[x] < -self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    def same(self, x, y):
        return self.find(x) == self.find(y)
    def size(self,x):
        return -self.parents[self.find(x)]


N, M = map(int,input().split())
A = sorted(list(map(int,input().split())))
uf = UnionFind(N)
all_sum = sum(A)

for i in range(N-1):
    if A[i] == A[i+1] or A[i+1] == A[i] + 1:
        uf.union(i, i+1)

if (A[N-1] + 1) % M == A[0]:
        uf.union(N - 1, 0)
        
sum_ = [0]*N

for i in range(N):
    root = uf.find(i)
    sum_[root] += A[i]

take = max(sum_)

ans = all_sum - take
print(ans)