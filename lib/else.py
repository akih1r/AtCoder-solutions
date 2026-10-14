

#中央値を求める
def solve_median(A):
    A.sort()
    half = len(A) // 2
    if len(A) % 2 == 0:
        return (A[half-1]+A[half]) / 2
    else:
        return A[half]


    