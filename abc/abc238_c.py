N = int(input())


S = [None]
for i in range(1,19):
  left = int("1"+ "0"*(i-1))
  right = int("9" * i)
  S.append((right - left + 1) * (right - left +1 + 1) // 2)

N_length = len(str(N))
ans = 0
for i in range(1, N_length-1+1):
  ans  += S[i] % 998244353#一個小さい桁までの和を含める

left = N
right = 10 ** (N_length -1)
ans += ((left - right + 1) * (left - right+1 +1) // 2) % 998244353

print(ans % 998244353)




  