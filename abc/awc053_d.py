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

#O(logn)で要素の挿入
#O(logn)で要素の削除
#O(1)で要素の存在確認
#O(1)で最小値の取得




import heapq
from sys import exit
class HeapDict:
    def __init__(self):
        self.h=[]
        self.d=dict()

    def insert(self,x):
        heapq.heappush(self.h,x)
        if x not in self.d:
            self.d[x]=1
        else:
            self.d[x]+=1

    def erase(self,x):
        if x not in self.d or self.d[x]==0:
            print(x,"is not in HeapDict")
            exit()
        else:
            self.d[x]-=1#すべてけしたいなら=０

        while len(self.h)!=0:
            if self.d[self.h[0]]==0:
                heapq.heappop(self.h)
            else:
                break

    def is_exist(self,x):
        if x in self.d and self.d[x]!=0:
            return True
        else:
            return False

    def get_min(self):
        return self.h[0]

N, M = map(int,input().split())
event = []
for i in range(M):
    l, r, c = map(int,input().split())
    event.append((l-1, i, "start", c))
    event.append((r,i,"end", c))

res = [0]*N
event.sort()
num_events = len(event)
hpdict = HeapDict()
hpdict.insert((float('inf'), 0))

cur_idx = 0
for i in range(N):
    while cur_idx < num_events and event[cur_idx][0] == i:
        where, idx, flag, c = event[cur_idx]
        if where == i:
            if flag == "start":
                hpdict.insert((-idx, c))
            else:
                hpdict.erase((-idx, c))
            cur_idx += 1
    
    
    order, c = hpdict.get_min()
    res[i] = c

print(*res)
            
    
        
        
    
        
