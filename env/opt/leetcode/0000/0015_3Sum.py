class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = list()
        nums.sort()
        n = len(nums)
        for i in range(n):
            target = 0 - nums[i]
            items = self.twoSum(nums[i+1:], target)
            for item in items:
                item.append(nums[i])
                if item not in ret:a
                    ret.append(item)
        return ret
        
    def twoSum(self, nums:List[int], target) -> List[List[int]]:
        ret = []
        if len(nums) < 2:
            return ret
        
        l_i = 0
        r_i = len(nums) - 1
        while l_i < r_i:
            sumv = nums[l_i] + nums[r_i]
            if sumv == target:
                ret.append([nums[l_i], nums[r_i]])
                l_i += 1
            elif sumv < target:
                l_i += 1
            else:
                r_i -= 1
        return ret 
            
        