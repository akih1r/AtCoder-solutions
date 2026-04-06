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
N, K = map(int, input().split())
BA = []
for _ in range(N):
  a, b = map(int, input().split())
  BA.append((b, a))
BA.sort(reverse=True)

q = []
#防御力の大きいものからK個とる
for _, a in BA[:K]:
  heapq.heappush(q, a)

s = sum(q)
#初期値は防御力の低い人がk人いると仮定（）
ans = s * BA[K-1][0]

#
for b, a in BA[K:]:
  s += a  #決めたM以上のｂ_iのときのa_iがくる
  s -= heapq.heappushpop(q, a)  #しかし小さいa_iはすてられるつまり上位K（において）を保持
  ans = max(ans, s * b)

print(ans)
