# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        for a in range(n):
            bs = list(range(n))
            del bs[a]
            ans = True
            if all(map(lambda x: knows(x, a), bs)) and \
                   all(map(lambda x: not knows(a, x), bs)):
                return a
        return -1