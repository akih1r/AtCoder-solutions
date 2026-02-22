import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
#N=int(input())
#N, M= map(int,input().split())
#A = list(map(int,input().split()))
#ls = [list(map(int, input().split())) for _ in range(N)]
#grid = [list(input()) for _ in range(N)]
#alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#N, A = map(int,input().split())
#X = list(map(int,input().split()))


#bit全探索
S = list(input())
N = len(S)
ans = 0
for bit in range(1 << N-1):
        
        res = S[0]
        
        for i in range(N-1):
            if (bit >> i) & 1:
                res += "+"
            res += S[i+1]
        current_val = sum(map(int, res.split("+")))
        ans += current_val

print(ans)
        