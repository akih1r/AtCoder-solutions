import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math

#=======================================================
#
#N=int(input())
#A =list(map(int,input().split()))
#ls = [list(map(int, input().split())) for _ in range(N)]
#grid = [list(input()) for _ in range(N)]
#alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#N, A = map(int,input().split())
#G = defaultdict(list)
#for i in range(M):
#    u, v = map(int,input().split())
#    G[u].append(v)
#    G[v].append(u)
#
#=========================================================


#M回をどう割り振るかの問題
#Fiを大きい順にソート
#Fi+1 <= Fi - (k-1)*Diの間はiをとりつづける
#Fi-Fi+1のなかに何個(k-1)*Diがある？
#もしｃ個分あったら数式いじってfi = F[i]+c*F[i]-(0.5*c*(c+1)*D[i])-D[i]*c)
#c=（F[i]-F[i+1]）// D[i]
#貪欲では？
#->Diについてもかんがえると違った
#ヒープ貪欲みたいです


import heapq

# 入力の読み込み
line = input().split()
if line:
    N, M = map(int, line)

    # (現在の収穫量, 疲弊度) のペアを格納するキュー
    # Pythonのheapqは最小値を取り出すため、収穫量をマイナスにして最大値を取り出せるようにする
    que = []
    for i in range(N):
        f, d = map(int, input().split())
        heapq.heappush(que, (-f, d))

    ans = 0
    count = 0

    # M回収穫を繰り返す
    while count < M and que:
        # 現在の最大収穫量を持つ木を取り出す
        neg_val, d = heapq.heappop(que)
        val = -neg_val
        
        # 合計に加算
        ans += val
        count += 1
        
        # 次の収穫量を計算
        next_val = val - d
        
        # 次の収穫量も0より大きいなら、更新してキューに戻す
        if next_val > 0:
            heapq.heappush(que, (-next_val, d))

    print(ans)