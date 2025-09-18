import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations
sys.setrecursionlimit(10**7)
#区間スケジュール問題
#締め切りが早い順にソート
N = int(input())
l = []
for i in range(N):
    a, b = map(int,input().split())
    l.append((a, b))

l = sorted(l, key=lambda x: x[1])

time = 0
cnt = 0
for a, b in l:
    if time+a <= b:
        time += a
        cnt += 1
    else:
        print("No")
        exit()
else:
    print("Yes")
    exit()
    