import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations
sys.setrecursionlimit(10**7)

S = list(input())

stack = []
for ch in S:
    stack.append(ch)
    while len(stack) >= 3 and stack[-3] == 'A' and stack[-2] == 'B' and stack[-1] == 'C':
        stack.pop(); stack.pop(); stack.pop()

print(''.join(stack))