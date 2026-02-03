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

S = input()


while S:
    if S.endswith("dream"):
        S = S[:-5]
    elif S.endswith("dreamer"):
        S = S[:-7]
    elif S.endswith("erase"):
        S = S[:-5]
    elif S.endswith("eraser"):
        S = S[:-6]
    else:
        print("NO")
        exit()

print("YES")