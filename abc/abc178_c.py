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

def solve():
    N = int(sys.stdin.readline())
    MOD = 1000000007

    
    term1 = pow(10, N, MOD)
    term2 = 2 * pow(9, N, MOD)
    term3 = pow(8, N, MOD)

    ans = (term1 - term2 + term3) % MOD
    
    print(ans)


solve()