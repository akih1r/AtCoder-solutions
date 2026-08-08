import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
from sortedcontainers import SortedSet, SortedList, SortedDict

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
#lst = sorted(lst, key=lambda x:x[1], reverse = True)
#=========================================================

"""
1. 目的


2. それに関わる特徴、性質は？
3000まで先頭からみていくと、iのときc[i-1]候補が多い
しかしその候補は高々3000個なので3000＾２でDPできる

3. 目的が達成するためにその性質をどう用いたら良いか？

4. 具体的にどう実装する？
一回普通にDPしてみる
3000よりは大きくなるので辞書で管理？
add = （bi - max(ai, 末尾のｃ)）
dp[iまで][c] = dp[i-1][末尾のc] + add
ここで問題発生ｃを範囲的に遷移させないといけない
こういうのはBITで解決したおぼえがある
→累積和でできるらしい

"""

import sys
from itertools import accumulate

def main():
    data = sys.stdin.buffer.read().split()
    MOD = 998244353
    V = 3001

    N = int(data[0])
    a = list(map(int, data[1:1 + N]))
    b = list(map(int, data[1 + N:1 + 2 * N]))

    
    dp = [[0] * 3001 for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        rui = list(accumulate(dp[i]))
        for nxt in range(a[i], b[i] + 1):
            dp[i + 1][nxt] = rui[nxt] % MOD
    ans = sum(dp[N]) % MOD

    print(ans)

main()