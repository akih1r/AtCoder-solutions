import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations
sys.setrecursionlimit(10**7)

#区間数え上げ,
#同じ余りが出るたびに、過去の同じ余りすべてと新しい区間が1つずつ作られる

N, M = map(int, input().split())
A = list(map(int, input().split()))

cnt = defaultdict(int)
cnt[0] = 1  # 累積和0（最初の状態）
ans = 0
sm = 0

for a in A:
    sm = (sm + a) % M     # 累積和の余り
    ans += cnt[sm]        # 同じ余りの個数を足す
    cnt[sm] += 1          # 現在の余りをカウント

print(ans)
