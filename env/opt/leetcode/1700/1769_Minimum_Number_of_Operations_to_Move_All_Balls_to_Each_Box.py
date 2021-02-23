class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = []
        for i in range(len(boxes)):
            ops = 0
            for j, ball in enumerate(boxes):
                if ball == "1":
                    ops += abs(i - j)
            # print(ops)
            ans.append(ops)
        return ans
        