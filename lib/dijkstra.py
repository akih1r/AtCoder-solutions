
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
    length = defaultdict(lambda: float("inf"))
    
    # 準備＝＝＝＝＝＝＝＝＝＝
    length[start] = 0 # スタートの長さは0
    hp = []
    heapq.heappush(hp, (0, start)) # (重み, ノード番号)
    # ＝＝＝＝＝＝＝＝＝＝＝＝

    while hp:
        w, x = heapq.heappop(hp)
        
        # 既に訪問済みならスキップ
        if x in visit:
            continue
        visit.add(x)
        
        # 【オプション】ゴールに着いたらそこで計算を打ち切る場合
        # if x == finish:
        #    return length[x]

        # table[x] から (重み l, 行き先 y) を取り出す
        for l, y in G[x]:
            # defaultdictなので length[y] は未探索なら自動で inf になる
            if y not in visit and length[y] > w + l:
                length[y] = w + l
                heapq.heappush(hp, (length[y], y))

    # 戻り値のパターン
    # return length[finish] # ゴールまでの最短経路のみ返す場合（到達不可ならinf）
    # return length # 全ノードの最短経路情報を辞書で返す場合
    