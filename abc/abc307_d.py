import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations
sys.setrecursionlimit(10**7)

#[解放]s
# (()...())とまたがっているものの数を取得したいときはスタックをつかうとよい
#末尾が条件を満たすと抽出

N = int(input())
S = list(input())

stack = []
start = 0
flag = False
for ch in S:
    stack.append(ch)
    if ch == "(":
        flag = True
        start += 1
        continue
    if flag:
        if ch == ')':
            while True:
                a = stack.pop()
                if a == "(":
                    break
            start -= 1
        if start <= 0:
            flag = False
print(''.join(stack))

