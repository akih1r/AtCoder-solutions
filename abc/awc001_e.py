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

import sys
from collections import deque

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    N, K = data[0], data[1]
    H = data[2:2+N]

    maxdq = deque()  # indices, H values decreasing
    mindq = deque()  # indices, H values increasing

    ans = 0
    for i, x in enumerate(H):
        while maxdq and H[maxdq[-1]] <= x:
            maxdq.pop()
        maxdq.append(i)

        while mindq and H[mindq[-1]] >= x:
            mindq.pop()
        mindq.append(i)

        left = i - K + 1
        if left >= 0:
            while maxdq[0] < left:
                maxdq.popleft()
            while mindq[0] < left:
                mindq.popleft()
            diff = H[maxdq[0]] - H[mindq[0]]
            if diff > ans:
                ans = diff

    print(ans)

if __name__ == "__main__":
    main()
