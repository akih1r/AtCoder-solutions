import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
#N=int(input())
#N, M= map(int,input().split())
#A = list(map(int,input().split()))
#ls = [list(map(int, input().split())) for _ in range(N)]
#grid = [list(input()) for _ in range(N)]
#alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#N, A = map(int,input().split())
#X = list(map(int,input().split()))

from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
d = defaultdict(int)
"""
dp[末尾の要素が v ] = 最大の長さ
それぞれの要素が末尾であるときの最大の長さをみる。
初期化は必要ない
i = 0のときdp[0-1]をみてなにもないので＋１で１になる
i = 1のときA[1]-1になるdpがないかをみるあったら＋１なかったらそのまま０
"""
for v in a:
    d[v] = max(d[v], d[v - 1] + 1)
print(max(d.values()))
