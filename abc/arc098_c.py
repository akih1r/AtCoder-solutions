import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
N=int(input())
#N, M= map(int,input().split())

#A = [0] + list(map(int,input().split()))

#ls = [list(map(int, input().split())) for _ in range(N)]
#grid = [list(input()) for _ in range(N)]
#alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

S = list(input())

#i個目までのW,Eの数累積リスト
num_w = 0
num_e = 0
acc = []
for i in range(N):
    if S[i] == "W":
        num_w += 1
    else:
        num_e += 1
    acc.append((num_w, num_e))

cnt = Counter(S)
sum_w = cnt["W"]
sum_e = cnt["E"]
me_w = 0
me_e = 0
mx = -1
for i in range(N):
    num_w_left, num_e_left = acc[i]
    if S[i] == "W":
        num_w_left -= 1
    else:
        num_e_left -= 1
        
    num_w_right = (sum_w) - acc[i][0]
    
    if num_w_right + num_e_left > mx:
        mx = num_w_right + num_e_left
        mx_idx = i


num_w_left, num_e_left = acc[mx_idx]
if S[mx_idx] == "W":
    num_w_left -= 1
else:
    num_e_left -= 1

num_e_right = (sum_e) - acc[mx_idx][1]

print(num_w_left + num_e_right)

    
    


    