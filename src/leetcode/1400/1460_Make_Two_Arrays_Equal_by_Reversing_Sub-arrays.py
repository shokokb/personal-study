class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        cnt_target = collections.Counter(target)
        cnt_arr    = collections.Counter(arr)
        for num in cnt_target.keys():
            if cnt_target[num] > cnt_arr[num]:
                return False
        return True
        