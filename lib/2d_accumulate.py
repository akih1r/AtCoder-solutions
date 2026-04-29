def sum2d(xl, yl, xr, yr, s):#左上s[xl][yl]左下s[xr][yl]右上s[xl][yr]右下s[xr][yr]
    res = 0
    res += s[xr][yr]
    res -= s[xl - 1][yr]
    res -= s[xr][yl - 1]
    res += s[xl - 1][yl - 1]
    return res

N, M, K = map(int, input().split())

# 0行目
s = [[0] * (M + 1)]

for _ in range(N):
    S = input()
    s.append([0] + list(accumulate(int(x) for x in S)))

# 縦方向の累積和はループで処理
for i in range(1, N + 1):
    for j in range(1, M + 1):
        s[i][j] += s[i - 1][j]