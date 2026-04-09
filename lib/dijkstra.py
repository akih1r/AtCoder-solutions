
from collections import defaultdict
import heapq
N, M = map(int,input().split())
G = [[] for i in range(N)]
for i in range(M):
    u, v, c = map(int,input().split())
    G[u].append((c, v))
    
    


def dijkstra(G, start, finish):
    # 訪問管理：setを使うと、ノードIDが飛び飛びでも対応可能
    visit = set()
    
    # 最短経路の長さ：アクセスした瞬間に初期値 inf が入る辞書を作成
    cost = defaultdict(lambda: float("inf"))
    
    # 準備＝＝＝＝＝＝＝＝＝＝
    cost[start] = 0 # スタートの長さは0
    hp = []
    heapq.heappush(hp, (0, start)) # (重み, ノード番号)
    # ＝＝＝＝＝＝＝＝＝＝＝＝

    while hp:
        now_cost, now = heapq.heappop(hp)
        
        # 既に訪問済みならスキップ
        if now in visit:
            continue
        visit.add(now)
        
        # 【オプション】ゴールに着いたらそこで計算を打ち切る場合
        # if x == finish:
        #    return cost[x]

        # G[x] から (重み w, 行き先 nex) を取り出す
        for w, nex in G[now]:
            # defaultdictなので cost[y] は未探索なら自動で inf になる
            if nex not in visit and cost[nex] > now_cost + w:
                cost[nex] = now_cost + w
                heapq.heappush(hp, (cost[nex], nex))

    # 戻り値のパターン
    # return cost[finish] # ゴールまでの最短経路のみ返す場合（到達不可ならinf）
    # return cost # 全ノードの最短経路情報を辞書で返す場合
    