import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations
sys.setrecursionlimit(10**7)
#import numpy as np
#N = int(input())
#S = list(input())
#N, Q = map(int,input().split())
#A = list(map(int,input().split()))
#S = [list(input()) for i in range(N)]

#[解放]
# (()...())とまたがっているものの数を取得したいときはスタックをつかうとよい
#末尾が条件を満たすと抽出

N = int(input())
S = input().strip()

stack = []
ans = 0
for ch in S:
    stack.append(ch)
    if len(stack) >= 3 and stack[-3:] == ['f', 'o', 'x']:
        stack.pop(); stack.pop(); stack.pop()
        ans += 1

# 残った長さ
print(len(stack))


