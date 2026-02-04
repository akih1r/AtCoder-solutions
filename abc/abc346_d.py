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

# 入力を高速に受け取る
input = sys.stdin.readline

def solve():
    # 入力
    try:
        line = input().strip()
        if not line: return
        n = int(line)
    except ValueError:
        return
        
    s = input().strip()
    c = list(map(int, input().split()))

    # DPテーブルの初期化
    # dp[j][k] : 重複が j 回で、最後の文字が k である最小コスト
    # j は 0 か 1, k は 0 か 1
    INF = float('inf')
    dp = [[INF] * 2 for _ in range(2)]

    # 1文字目 (i=0) の初期化
    # 重複(j)はまだ0回。
    # 0にするコスト: 元が'1'ならかかる
    cost0 = c[0] if s[0] == '1' else 0
    dp[0][0] = cost0
    
    # 1にするコスト: 元が'0'ならかかる
    cost1 = c[0] if s[0] == '0' else 0
    dp[0][1] = cost1

    # 2文字目からN文字目までループ
    for i in range(1, n):
        # 新しいDPテーブル（更新用）
        new_dp = [[INF] * 2 for _ in range(2)]
        
        # i文字目を 0 にするコスト、1 にするコスト
        cost_make_0 = c[i] if s[i] == '1' else 0
        cost_make_1 = c[i] if s[i] == '0' else 0
        
        # --- 遷移 ---
        
        # 【ケース1: 今回を 0 にする場合 (k=0)】
        # 1-A: 前回が 0 (prev_k=0) -> 0と0で被る -> jは +1 される
        #      今の j=1 になれるのは、前が j=0 のときだけ
        if dp[0][0] != INF:
            new_dp[1][0] = min(new_dp[1][0], dp[0][0] + cost_make_0)
            # もし前ですでに j=1 だったら、今回さらに被って j=2 になるのでアウト（計算不要）
            
        # 1-B: 前回が 1 (prev_k=1) -> 1と0で被らない -> jはそのまま
        if dp[0][1] != INF:
            new_dp[0][0] = min(new_dp[0][0], dp[0][1] + cost_make_0)
        if dp[1][1] != INF:
            new_dp[1][0] = min(new_dp[1][0], dp[1][1] + cost_make_0)

        # 【ケース2: 今回を 1 にする場合 (k=1)】
        # 2-A: 前回が 0 (prev_k=0) -> 0と1で被らない -> jはそのまま
        if dp[0][0] != INF:
            new_dp[0][1] = min(new_dp[0][1], dp[0][0] + cost_make_1)
        if dp[1][0] != INF:
            new_dp[1][1] = min(new_dp[1][1], dp[1][0] + cost_make_1)

        # 2-B: 前回が 1 (prev_k=1) -> 1と1で被る -> jは +1 される
        if dp[0][1] != INF:
            new_dp[1][1] = min(new_dp[1][1], dp[0][1] + cost_make_1)

        # テーブル更新
        dp = new_dp

    # 答えは、最後まで見て「重複がちょうど1回 (j=1)」であるものの最小値
    # 最後が0の場合と1の場合の小さい方
    ans = min(dp[1][0], dp[1][1])
    
    print(ans)

if __name__ == '__main__':
    solve()