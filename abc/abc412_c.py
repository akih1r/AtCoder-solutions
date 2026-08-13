import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
from sortedcontainers import SortedSet, SortedList, SortedDict

#=======================================================
#
# N=int(input())
# A =list(map(int,input().split()))
# S = [0] + accmulate(A)
# ls = [list(map(int, input().split())) for _ in range(N)]
# grid = [list(input()) for _ in range(N)]
# alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
# N, M, T = map(int,input().split())
# G = defaultdict(list)
# for i in range(M):
#     u, v = map(int,input().split())
#     G[u].append(v)
#     G[v].append(u)
# lst = sorted(lst, key=lambda x:x[1], reverse = True)
#=========================================================

"""
1 何ごとの話にすると見やすい？なにだけ持てばいい？
ABC412C
まず判定問題を解く最終的にNがたおれればいいから逆から考える
まずNがたおれるにはceil(S[N]/2)以上である必要がある
その中で最小をとりまたceil(S[N]/2)以上が存在するかをみる
もし最小ととってそれが２S[1]＞＝S[now]なら到達可能で終了
到達しない場合を考える
候補がひとつもない時点で終了

２S[1]＞＝S[now]なら到達可能で終了この終了のときのcntはふやさないとして答えはcnt+2がこたえ

最小で何個？

Sからドミノ１、Nを削除後ソート探索するときは二分探索

上のステップ数でわかるのでは？



2 それについて、何がわかれば答えになる？


3 何を捨ててよく、なぜそれで足りる？何が効く？何が禁止？


4 その情報をそう更新/判定/集計すれば実装できる？

"""

T = int(input())
for _ in range(T):
    N = int(input())
    S = list(map(int,input().split()))
    first = S[0]
    last = S[-1]
    S_sorted = sorted(S[1:-1])
    step = 0
    hi = len(S_sorted)
    while True:
        if 2* first >= last:
            print(step + 2)
            break
        want_v = (last + 2 -1) // 2 #切り上げ除算
        idx = bisect.bisect_left(S_sorted, want_v, 0, hi)
        #候補がないとき
        if idx >= hi:
            print(-1)
            break
        last = S_sorted[idx]
        hi = idx
        
        step += 1
    