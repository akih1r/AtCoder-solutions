

N = int(input())
P = list(map(int,input().split()))

dp = [0]*N
dp[1] = 0

for i in range(1,N):
    dp[i] = dp[P[i]] + 1

print(dp[N-1])
    