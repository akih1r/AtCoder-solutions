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
N頂点N辺だから閉路あり
最小距離がkであるものの距離の数
式１、最小距離がｋ以下の数ー最小距離がｋ未満の数　=最良距離がｋが使えそう
最小距離をもとめる？
O(N*N*logN)まではいける
iからBFSして式１をつかう
頂点iとi+1は必ず隣接している。ので距離が１
i<jがひっかかる＜－そんなにかんけいなかった
一回のBFSでiからj(>i)のすべては探索できそう重複はvisitedで管理したら楽か
ｋでループをまわす

あるiについてBFSそれぞれiからの距離を保管
最小距離がkであるものをさがす
距離の配列をソートして二分探索で式１をつかってｋの数をもとめる
2 それについて、何がわかれば答えになる？


3 何を捨ててよく、なぜそれで足りる？何が効く？何が禁止？


4 その情報をそう更新/判定/集計すれば実装できる？

"""

N, X, Y = map(int,input().split())
G = defaultdict(list)
for i in range(N-1):
    G[i].append(i+1)
    G[i+1].append(i)
G[X-1].append(Y-1)
G[Y-1].append(X-1)


def bfs(start, v_scale):
    que = deque([start])
    dist = [-1]*(v_scale+1)
    dist[start] = 0
    while que:
        now = que.popleft()
        for nxt in G[now]:
            if dist[nxt] == -1:
                dist[nxt] = dist[now]+1
                que.append(nxt)
    return dist



k_bucket = [0]*(N)
seen = set()
for i in range(N):
    # iを始点としたとき（i, j）の距離をしらべる
    dist = bfs(i, N)
    l = []
    for k, d in enumerate(dist):
        s, g = min(i,k), max(i, k)
        if (s, g) in seen:
            continue
        seen.add((s,g))
        if d != -1:
            l.append(d)
    l.sort()
    for k in range(1, N):
        #最小距離がｋ以下の数ー最小距離がｋ未満の数　=最良距離がｋ
        k_bucket[k] += bisect.bisect_right(l, k) - bisect.bisect_left(l, k)

for i in range(1,N):
    print(k_bucket[i])
    