import unittest

from typing import List

class Solution:
    # n = len(triangle)
    # Time Complexity = O(n^2)
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # dp = []
        # for i in range(len(triangle)):
        #     row = triangle[i]
        #     dp_in_row = []
        #     if i == 0:
        #         dp.append([row[i]])
        #     else :
        #         for j in range(len(row)):
        #             if j == 0 :
        #                 dp_in_row.append(dp[-1][0]+row[j])
        #             elif j == len(row)-1:
        #                 dp_in_row.append(dp[-1][-1]+row[j])
        #             else:
        #                 dp_in_row.append(min(dp[-1][j-1], dp[-1][j])+row[j])  
        #         dp.append(dp_in_row)
        # return min(dp[-1])
        dp = []
        for i in range(len(triangle)):
            row = triangle[i]
            dp_in_row = []
            if i == 0:
                dp = [row[i]]
            else :
                for j in range(len(row)):
                    if j == 0 :
                        dp_in_row.append(dp[0]+row[j])
                    elif j == len(row)-1:
                        dp_in_row.append(dp[-1]+row[j])
                    else:
                        dp_in_row.append(min(dp[j-1], dp[j])+row[j])  
                dp = dp_in_row
        return min(dp) # O(nlogn)


class TestSolution(unittest.TestCase):
    def testMinimumTotal(self):
        s = Solution()
        self.assertEqual(11, s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
        self.assertEqual(-10, s.minimumTotal([[-10]]))

def main():    
    unittest.main()

if __name__ == "__main__":
    main()