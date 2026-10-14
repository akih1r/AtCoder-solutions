import heapq
N, T = map(int,input().split())
events = []
for i in range(N):
    x, y = map(int,input().split())
    events.append((x,y))
#重なりの最大
events.sort()
ans = 0
hp = []
num = 0
for event in events:
    s, e = event
    now_t = s
    while hp and hp[0] <= now_t:
        heapq.heappop(hp)
    heapq.heappush(hp, e)
    ans = max(ans, len(hp))
print(ans)