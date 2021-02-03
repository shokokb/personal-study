class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt1 = collections.Counter(nums1)
        cnt2 = collections.Counter(nums2)
        ans = []
        for k in cnt1.keys():
            if cnt2[k] > 0:
                ans.extend([k])
        return ans
        