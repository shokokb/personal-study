class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        digits.sort(reverse = True)
        for i in range(len(digits), 0, -1):
            c = combinations(digits, i)
            for comb in c:
                if sum(comb) % 3 == 0:
                    if all([x == 0 for x in comb]):
                        return "0"
                    return "".join(map(lambda x: str(x), list(comb)))
        return ""
        