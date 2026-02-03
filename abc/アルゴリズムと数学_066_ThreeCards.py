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

N, K = map(int,input().split())
comb = 0
for black in range(1, N + 1):
    # 黒の範囲
    b_start = black - K + 1
    b_end   = black + K - 1
    
    b_start = max(1, b_start)
    b_end   = min(N, b_end)

    for white in range(b_start, b_end + 1):
        
        w_start = white - K + 1
        w_end   = white + K - 1
        
        common_start = max(b_start, w_start)
        common_end   = min(b_end, w_end)
        
        if common_start <= common_end:
            length = common_end - common_start + 1
            comb += length

print(N**3 - comb)
    