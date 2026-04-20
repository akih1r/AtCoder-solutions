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

T = int(input())
#括弧をはずす
def f(S):
    stack = []
    for i in range(len(S)):
        stack.append(S[i])
        if len(stack) >= 4 and stack[-1] == ")" and stack[-2] == "x" and stack[-3] == "x" and stack[-4] == "(":
            s1 = stack.pop()
            s2 = stack.pop()
            s3 = stack.pop()
            s4 = stack.pop()
            stack.append(s2)
            stack.append(s3)
    return stack

for i in range(T):
    A = list(input())
    B = list(input())
    if f(A) == f(B):
        print("Yes")
    else:
        print("No")
    