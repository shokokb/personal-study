class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l, r = 0, len(people)-1
        cnt = 0
        people.sort()
        while (l <= r):
            if people[r] + people[l] <= limit:
                l += 1
            cnt += 1
            r -= 1
        return cnt