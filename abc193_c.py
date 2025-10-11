import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations
sys.setrecursionlimit(10**7)

#「1 以上 N 以下の整数のうち、べき数でないものの数
#底が２からべき数
# 2^2, 2^3, 2^4....3^2, 3^3, 3^4....と列挙して判定し
# Nをその満たす数を引く。aは√Nまで探索（二乗するとNになるため）
N = int(input())
seen = set()

a = 2
while a * a <= N:
    val = a * a
    while val <= N:
        seen.add(val)
        val *= a
    a += 1

print(N - len(seen))
