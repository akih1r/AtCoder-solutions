#約数列挙
for _ in range(int(input())):
    n = int(input())
    d = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            d.append(i)
            if i != n // i:
                d.append(n // i)
        i += 1
    d.sort()



class Eratosthenes:
    def __init__(self, N):
        self.N = N
        mf = list(range(N + 1))          # 初期値は自分自身（mf[1] == 1 になるのが効く）
        for i in range(2, int(N**0.5) + 1):
            if mf[i] == i:               # まだ書き換わっていない = i は素数
                for j in range(i * i, N + 1, i):
                    if mf[j] == j:
                        mf[j] = i
        self.minfactor = mf

    def is_prime(self, n):
        return n > 1 and self.minfactor[n] == n

    def primes(self):
        return [i for i in range(2, self.N + 1) if self.minfactor[i] == i]

    def factorize(self, n):
        """n -> [(素数, 指数), ...]   n == 1 なら []"""
        mf = self.minfactor
        res = []
        while n > 1:
            p = mf[n]
            e = 0
            while mf[n] == p:            # mf[1] == 1 なので自然に止まる
                n //= p
                e += 1
            res.append((p, e))
        return res

    def divisors(self, n):
        res = [1]
        for p, e in self.factorize(n):
            res = [d * p**k for d in res for k in range(e + 1)]
        res.sort()
        return res

    def euler_phi(self, n):
        res = n
        for p, _ in self.factorize(n):
            res = res // p * (p - 1)
        return res