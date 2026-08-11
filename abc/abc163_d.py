import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
from sortedcontainers import SortedSet, SortedList, SortedDict

#=======================================================
#
# N=int(input())
# A =list(map(int,input().split()))
# S = [0] + accmulate(A)
# ls = [list(map(int, input().split())) for _ in range(N)]
# grid = [list(input()) for _ in range(N)]
# alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
# N, M, T = map(int,input().split())
# G = defaultdict(list)
# for i in range(M):
#     u, v = map(int,input().split())
#     G[u].append(v)
#     G[v].append(u)
# lst = sorted(lst, key=lambda x:x[1], reverse = True)
#=========================================================

"""
1 何ごとの話にすると見やすい？なにだけ持てばいい？
10^100乗があってもなくても和の種類は同じ
よって０からNについてかんがえるふつうにかんがえれば(N+1)_C_K通り
DP？でもdp[N][K]はまにあわないぞ
まてK個以上になってる
扱いにくいから全通りーK個未満でもよさそう
となるとK個未満であり得る和の数は？？
ここまで考察は全然ちがうらしい
いちから考え直す
10^100乗の係数とそれ以外に分ける
a* 10^100 + b
aの候補はK個以上選ぶので（a>= K）となり
aは（N+1から）選んだ個数である
bは０からNの組み合わせで　
０からNまでの和の種類はｎ＋（nー１）?
aとｂをひもづけたい
選んだものについて何個和が何個つくれるか
わからなくなってきた
(0,1,2,3,4,5)について
３個えらぶとき
(0,1,2)が最小＝３
（3,4,5）が最大 = 12 
３から１２のあいだは（,,）の組み合わせをかえると埋まって連続になるので
max - min+1 = sum([N-K+1,N]) - sum([0,K-1]) + 1 
2 それについて、何がわかれば答えになる？


3 何を捨ててよく、なぜそれで足りる？何が効く？何が禁止？


4 その情報をそう更新/判定/集計すれば実装できる？

"""
MOD = 10 **9 +7
N, K = map(int,input().split())
acc = list(accumulate(range(0, N+1)))
ans = 0
for k in range(K, N+2):
    #k個選ぶ
    if N-k >= 0:
        num_b = (acc[-1] - acc[N-k]) - acc[k-1] +1
    else:
        num_b = (acc[-1]) - acc[k-1] +1
    ans += num_b
    ans %= MOD
print(ans)