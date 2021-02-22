# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def isCelebrity(self, i, n):
        for j in range(n):
            if i == j:
                continue
            if knows(i, j) or not knows(j, i):
                return False
        return True
    def findCelebrity(self, n: int) -> int:
        celebrity_candicate = 0
        for i in range(1, n):
            if knows(celebrity_candicate, i):
                celebrity_candicate = i
        if self.isCelebrity(celebrity_candicate, n):
            return celebrity_candicate
        return -1