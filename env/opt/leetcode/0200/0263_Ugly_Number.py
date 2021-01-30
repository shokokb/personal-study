class Solution:
    def isUgly(self, num: int) -> bool:
        def prime_factorize(n):
            a = []
            while n % 2 == 0:
                a.append(2)
                n //= 2
            f = 3
            while f * f <= n:
                if n % f == 0:
                    a.append(f)
                    n //= f
                else:
                    f += 2
            if n != 1:
                a.append(n)
            return a
        if num > 0:
            ans = set(prime_factorize(num))
            return ans <= {2,3,5}
        else:
            return False
        