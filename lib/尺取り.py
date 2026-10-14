N, K = map(int,input().split())
A = list(map(int,input().split()))



#先読み条件を満たす最大長
r = 0
ans = 0
sum_ = 0
for l in range(N):
    while r < N and sum_ + A[r] <= K:#条件満たしてるか確認してから入れる
        sum_ += A[r]
        r += 1
    
    ans = max(r-l, ans)
    
    if l == r:
        r += 1
    else:
        sum_ -= A[l]
        

#先読みせずとりあえず伸ばして後で見る（最小長）


r = 0
ans = 10**20
sum_ = 0
for l in range(N):
    while r < N and sum_ <= K:#Kをこえたときの最小
        sum_ += A[r]
        r += 1
    
    if sum_ > K:
        ans = min(r-l, ans)
    
    if l == r:
        r += 1
    else:
        sum_ -= A[l]



N = int(input())
A = list(map(int,input().split()))


Q = deque()
ans = 0
for i in range(N):
    Q.append(A[i])
    while len(Q)>=2 and not (Q[-1] > Q[-2]):
        Q.popleft()
    ans += len(Q)
        

print(ans)