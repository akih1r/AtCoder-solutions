#めぐる式二分探索
def is_ok(ans, before, mid):
    return bool
    


def meguru_bisect(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

'''
最小化
[ng, ng, ..... ok, ok]のとき
つまり条件を満たす値の最小化
ng = min-1 ok = max+1
*コストをX円以下にできる最小の時間

最大化
[ok, ok, ... ng, ng]の時
つまり条件を満たす最大の値を求める
ok = min-1  ng = max+1
*所持金X円を超えない範囲で最大の価値
'''







#使用例
from itertools import combinations, permutations, accumulate
N, K = map(int,input().split())
A = [0] + list(map(int,input().split()))
B = [0] + list(map(int,input().split()))
S_A = list(accumulate(A))
S_B = list(accumulate(B))

#めぐる式二分探索
def is_ok(mid, l):
    return S_B[mid] - S_B[l-1] <= K    


def meguru_bisect(ng, ok, l):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid, l):
            ok = mid
        else:
            ng = mid
    return ok

rem = []
for l in range(1,N+1):
    idx = meguru_bisect(N+1, l-1, l)
    if idx >= l:
        rem.append((l, idx))


    