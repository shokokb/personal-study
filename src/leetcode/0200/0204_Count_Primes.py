import math
class Solution:
    def countPrimes(self, n: int) -> int:
        
        def is_prime (num:int) :
            if num < 2: return False
            elif num == 2: return True
            elif num % 2 == 0: return False

            sqrt_num = math.sqrt(num)
            for i in range(3, int(sqrt_num) + 1, 2):
                if num % i == 0:
                    return False
            return True
        
        cnt = 0
        for i in range(2, n):
            if is_prime(i):
                cnt += 1
        return cnt