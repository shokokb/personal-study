class FirstUnique:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def showFirstUnique(self) -> int:
        c = collections.Counter(self.nums)
        for n in self.nums:
            if c[n] == 1:
                return n
        return -1
        

    def add(self, value: int) -> None:
        self.nums.append(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)