N = int(input())
A = list(map(int,input().split()))

p = 0
for i in range(N):
    if A[i] == i+1:
      p += 1
    
cnt = p* (p-1)//2

for i in range(1,N+1):
  if A[i-1] > i and A[A[i-1]-1] == i:
    cnt += 1

print(cnt)