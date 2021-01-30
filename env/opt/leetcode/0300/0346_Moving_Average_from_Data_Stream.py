class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.cur_size = 0
        self.scores = [] 

    def next(self, val: int) -> float:
        self.scores.append(val)
        if self.cur_size < self.size:
            self.cur_size += 1
        return sum(self.scores[-self.cur_size:]) / self.cur_size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)