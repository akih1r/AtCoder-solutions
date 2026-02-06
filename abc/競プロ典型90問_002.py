import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
#N=int(input())
#N, M, P = map(int,input().split())
#A = list(map(int,input().split()))
#B = sorted(list(map(int,input().split())))

#ls = [list(map(int, input().split())) for _ in range(N)]
#grid = [list(input()) for _ in range(N)]
#alpha = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]

from itertools import product

# カッコ列 S が整合しているかどうか
def isvalid(S):
    score = 0
    for c in S:
        if c == '(':
            score += 1
        else:
            score -= 1

        # 途中で 0 を下回るとダメ
        if score < 0:
            return False

    # 最後に 0 なら True、そうでなければ False
    return (score == 0)

N = int(input())
for S in product(['(', ')'], repeat=N):
    if (isvalid(S)):
        # リストを文字列に
        print(*S, sep='')