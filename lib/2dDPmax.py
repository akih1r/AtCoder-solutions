



#dp[i][j] i個まで考慮して、j分の時間をかけた
#ans = max(dp[N])

N, M = map(int,input().split())
R, T = [], []
for i in range(N):
    r, t = map(int,input().split())
    R.append(r); T.append(t)

dp = [[-1]*(M+1) for i in range(N+1)]
R = [-1]+R
T = [-1]+T
dp[0][0] = 0

for i in range(N):
    for j in range(M+1):
        if dp[i][j] == -1:
            continue
        #i個目を選ばない
        dp[i+1][j] = max(dp[i][j],dp[i+1][j])
        #i個目を選ぶ
        if j+ T[i+1] <= M and j < M:
            dp[i+1][j+T[i+1]] = max(dp[i][j] + R[i+1],dp[i+1][j+T[i+1]])

ans = max(dp[N])
print(ans)
