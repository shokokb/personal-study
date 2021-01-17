class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        s = {n for n in range(1, len(nums) + 1)}
        
        seen = set()
        for n in nums:
            if n in seen:
                return [n, (s-set(nums)).pop()]                
            seen.add(n)
        