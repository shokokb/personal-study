class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnt = collections.Counter(nums)
        cnt = sorted(cnt.items(), key=lambda x: x[1])
        d = defaultdict(lambda:[])
        for num, time in cnt:
            d[time].append(num)
        s = []
        for time in d.keys():
            nums = d[time]
            nums.sort(reverse=True)
            for num in nums:            
                s.extend([num] * time) 
        return s        