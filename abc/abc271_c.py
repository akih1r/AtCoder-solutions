import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations
sys.setrecursionlimit(10**7)


def is_ok(m):
    # m 巻まで読めるか？
    c = len(set(range(1, m + 1)) & A)
    return c + (N - c) // 2 >= m #「持っている冊数 (c) + 作れる冊数 ( (N-c)//2 )」が、必要な冊数 m を満たせば読める。


def meguru_bisect(ok, ng):
    # 最大の OK を返す
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


N = int(input())
A = set(map(int, input().split()))

print(meguru_bisect(0, N + 1))
