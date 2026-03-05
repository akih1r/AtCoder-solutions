import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
#N=int(input())
#N, M= map(int,input().split())
#A = list(map(int,input().split()))
#ls = [list(map(int, input().split())) for _ in range(N)]
#grid = [list(input()) for _ in range(N)]
#alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#N, A = map(int,input().split())
#X = list(map(int,input().split()))
N, M = map(int,input().split())
qr = []
for i in range(M):
    a, b, c = map(int,input().split())
    a -= 1
    b -= 1
    qr.append((a,b,c))

qr.sort(key= lambda x : x[2])

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

uf = UnionFind(N)
point = 0
for a, b, c in qr:
    if c < 0:
        uf.union(a, b)
        continue
    if not uf.same(a,b):
        uf.union(a,b)
    else:
        point += c

print(point)