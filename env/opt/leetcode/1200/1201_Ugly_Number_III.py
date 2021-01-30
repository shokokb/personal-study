class Solution:        
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        nums = [1]
        seen = {1}
        i_a, i_b, i_c = 1, 1, 1
                
        for i in range(n):
            minv = min (a * i_a, b * i_b, c * i_c)
            if minv == a * i_a:
                i_a += 1
            if minv == b * i_b:
                i_b += 1
            if minv == c * i_c:
                i_c += 1
            if minv not in seen:
                nums.append(minv)
                seen.add(minv)
        return nums[n]
