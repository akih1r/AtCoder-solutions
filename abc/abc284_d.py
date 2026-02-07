import sys, bisect, heapq
from collections import defaultdict, deque, OrderedDict, Counter
from itertools import combinations, permutations, accumulate
sys.setrecursionlimit(10**7)
import math
#N=int(input())
#N, M, P = map(int,input().split())
#A = list(map(int,input().split()))
#B = sorted(list(map(int,input().split())))

#ls = [list(map(int, input().split())) for _ in range(N)]
#grid = [list(input()) for _ in range(N)]
#alpha = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]

import sys
import math

# 入力を高速に読み込むおまじない
input = sys.stdin.read

def main():
    data = input().split()
    iterator = iter(data)

    # テストケース数 T
    try:
        t = int(next(iterator))
    except StopIteration:
        return

    results = []

    for _ in range(t):
        n = int(next(iterator))
        
        p = 0
        q = 0
        i = 2
        
        # C++の for(long long i=2; i*i*i <= n; i++) に相当
        while i * i * i <= n:
            if n % i == 0:
                # 割り切れた（i は p か q のどちらか）
                
                if (n // i) % i == 0:
                    # i^2 で割り切れる場合 -> p = i
                    p = i
                    q = n // (i * i)
                else:
                    # i でしか割り切れない場合 -> q = i
                    q = i
                    # p = sqrt(n / i)
                    p = math.isqrt(n // i)
                
                # 見つかったらループ終了
                break
            
            i += 1

        results.append(f"{p} {q}")

    # 結果をまとめて出力
    print('\n'.join(results))

if __name__ == '__main__':
    main()