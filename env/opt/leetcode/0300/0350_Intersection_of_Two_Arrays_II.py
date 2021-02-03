class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt1 = collections.Counter(nums1)
        cnt2 = collections.Counter(nums2)
        ans = []
        for k in cnt1.keys():
            count = min(cnt1[k], cnt2[k])
            ans.extend([k] * count)
        return ans
        