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
Kを経由したときの最短距離ｘ、ｙ
KからBFSしてｘ＋ｋとK＋Yを記録？
コストもあるのか。。。ダイクストラでごりおす？

2 それについて、何がわかれば答えになる？


3 何を捨ててよく、なぜそれで足りる？何が効く？何が禁止？


4 その情報をそう更新/判定/集計すれば実装できる？

"""


from collections import defaultdict
import heapq
N = int(input())
G = [[] for i in range(N+1)]
for i in range(N-1):
    u, v, c = map(int,input().split())
    G[u].append((c, v))
    G[v].append((c, u))
    


def dijkstra(G, start):
    # 訪問管理：setを使うと、ノードIDが飛び飛びでも対応可能
    visit = set()
    
    # 最短経路の長さ：アクセスした瞬間に初期値 inf が入る辞書を作成
    cost = defaultdict(lambda: float("inf"))
    
    cost[start] = 0 # スタートの長さは0
    hp = []
    heapq.heappush(hp, (0, start)) # (重み, ノード番号)

    while hp:
        now_cost, now = heapq.heappop(hp)
        
        # 既に訪問済みならスキップ
        if now in visit:
            continue
        visit.add(now)
        

        # G[x] から (重み w, 行き先 nex) を取り出す
        for w, nex in G[now]:
            # defaultdictなので cost[y] は未探索なら自動で inf になる
            if nex not in visit and cost[nex] > now_cost + w:
                cost[nex] = now_cost + w
                heapq.heappush(hp, (cost[nex], nex))

    return cost

Q, K = map(int,input().split())
cost = dijkstra(G, K)

for i in range(Q):
    x, y = map(int,input().split())
    print(cost[x]+cost[y])