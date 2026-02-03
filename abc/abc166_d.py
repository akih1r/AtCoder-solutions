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


x = int(sys.stdin.readline())

mp = {}

for i in range(999, -1, -1):
    c = i ** 5
    
    # パターン1: B = i の場合
    if (c + x) in mp:
        print(mp[c + x], i)
        exit()
    
    # パターン2: B = -i の場合
    if (x - c) in mp:
        print(mp[x - c], -i)
        exit()
        
    # 現在の i を A の候補として辞書に登録
    mp[c] = i