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



N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))
#xセンチ以上単位で切れるか前からみる。
def cut_with(x):
    num = 0
    pre = 0 #前回切った場所を保存し、そこからｘセンチ以上ｓるか見て切る
    for i in range(N):
        if A[i] - pre >= x:
            num += 1
            pre = A[i]
    
    if L - pre >= x:
        num += 1
    
    return (num >= K + 1)


#xセンチについて二分探索条件を満たすｘの最大化
def meguru_bisect(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    '''
    
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if cut_with(mid):
            ok = mid
        else:
            ng = mid
    return ok
print(meguru_bisect(L+1, -1))
'''
最小化
[ng, ng, ..... ok, ok]のとき
つまり条件を満たす値の最小化
ng = min-1 ok = max+1
*コストをX円以下にできる最小の時間

最大化
[ok, ok, ... ng, ng]の時
つまり条件を満たす最大の値を求める
ok = min-1  ng = max+1
*所持金X円を超えない範囲で最大の価値
'''
        
        
        