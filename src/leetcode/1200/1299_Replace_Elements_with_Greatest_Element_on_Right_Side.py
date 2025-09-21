class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ret = []
        d = deque()
        for i in range(len(arr) - 1, -1, -1):
            if i == len(arr) - 1:
                d.appendleft(-1)
                continue
            d.appendleft(max(arr[i+1], d[0]))
        return list(d)