import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
#N=int(input())
#N, K= map(int,input().split())
#D = list(map(int,input().split()))
#B = list(map(int,input().split()))

#ls = [list(map(int, input().split())) for _ in range(N)]
#grid = [list(input()) for _ in range(N)]
#alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


import math

def num(n, c, d):
    g = math.gcd(c, d)
    l = (c * d) // g
    
    return n - (n // c) - (n // d) + (n // l)

a, b, c, d = map(int, input().split())

print(num(b, c, d) - num(a - 1, c, d))