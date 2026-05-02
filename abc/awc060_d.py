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
#=========================================================



N = int(input())
P, Q = [], []
for _ in range(N):
  p, q = map(int, input().split())
  P.append(p)
  Q.append(q)

ans = 100
#bit全探索　N＜＝20くらいならいける
for s in range(1<<N):
  if s.bit_count() <= 1: #ビット列に１が何個あるか２個なかったら飛ばす
    continue
  x, y = 1, 1
  for i in range(N):
    if s & (1<<i):
      x *= P[i]
      y *= Q[i]
  if x == y:
    ans = min(ans, s.bit_count())

if ans == 100:
  print(-1)
else:
  print(ans)
