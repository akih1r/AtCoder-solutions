import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math

#=======================================================
#
#N=int(input())
#A =list(map(int,input().split()))
#S = [0] + accmulate(A)
#ls = [list(map(int, input().split())) for _ in range(N)]
#grid = [list(input()) for _ in range(N)]
#alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#N, M, T = map(int,input().split())
#G = defaultdict(list)
#for i in range(M):
#    u, v = map(int,input().split())
#    G[u].append(v)
#    G[v].append(u)
#
#=========================================================import heapq




from collections import defaultdict
import heapq
N, M = map(int,input().split())
G = [[] for i in range(N+1)]
for i in range(M):
    u, v, c = map(int,input().split())
    G[u].append((c, v))
    G[v].append((c, u))

def dijkstra(G, start, finish):
    visit = set()
    dp = [[float("inf")]*2 for i in range(N+1)]
    dp[start][0] = 0 # スタートの長さは0
    hp = []
    heapq.heappush(hp, (0, start, 0)) # (重み, ノード番号)
    while hp:
        w, x, flag = heapq.heappop(hp)
        
        # 既に訪問済みならスキップ
        if (x, flag) in visit:
            continue
        visit.add((x, flag))
        
        if x == finish:
            continue
        
        if flag == 1:#もう無料をつかった
            for l, y in G[x]:
                if (y, flag) not in visit and dp[y][1] > w + l:
                    dp[y][1] = min(w + l, dp[y][1])
                    heapq.heappush(hp, (dp[y][1], y, 1))
                    
        else:#まだつかってない
            for l, y in G[x]:
                if dp[y][1] > w and (y, 1) not in visit:
                    #使う
                    dp[y][1] = w
                    heapq.heappush(hp, (dp[y][1], y, 1))
                
                if dp[y][0] > w+l and (y, 0) not in visit:
                    dp[y][0] = w+l
                    heapq.heappush(hp, (dp[y][0], y, 0))
                    
    return dp
dp = dijkstra(G, 1, N)
ans = min(dp[N])
if ans == float("inf"):
    print(-1)
else:
    print(ans)