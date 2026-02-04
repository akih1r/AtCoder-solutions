import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
#N=int(input())
#N, T = map(int,input().split())
#A = list(map(int,input().split()))
#ls = [list(map(int, input().split())) for _ in range(N)]
#grid = [list(input()) for _ in range(N)]
#alpha = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]

import sys


data = sys.stdin.read().split()
N = int(data[0])
S = data[1::2]
T = data[2::2]


G = {}
for s, t in zip(S, T):
    G[s] = t

#  閉路検出

visited = set()

for start_node in list(G.keys()):
    if start_node in visited:
        continue

    curr = start_node
    path = set() 

    while curr in G:
        if curr in path:
            print("No")
            sys.exit()
        
        
        if curr in visited:
            break
            
        path.add(curr)    
        curr = G[curr]    
    
    visited.update(path)

print("Yes")