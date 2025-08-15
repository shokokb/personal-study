# 7. Reverse Integer

import unittest

# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
class Solution:
    def reverse(self, x: int) -> int:
        ret = 0

        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        # 1.文字列で反転する方法
        # str() で文字列にして、[::-1] で反転
        text = str(x)[::-1]
         
        # 符号は別にして、最後に戻す
        if text[-1] == "-":
            text = "-" + text[:-1]
        ret = int(text)

        # int() に変換後、範囲チェック
        if ret < INT_MIN or INT_MAX > ret:
            ret = 0

        return ret

        # 2. 数学的に反転する方法（10進の剰余・除算）
        # while ループで n % 10 を取り出して末尾に追加
        # n //= 10 で1桁ずつ削る
        # 新しい数字を構築しながら範囲チェック
        # 実装はまだ
        # sign = 1
        # number = 0
        
        # if x < 0:
        #     sign = -1
        #     x *= -1

        # n = 0

        # while x > 0:
        #     mod = x % 10
        #     x = x // 10
        #     number += mod * 10 ** n
        #     n += 1

        return ret
            
class TestSolution(unittest.TestCase):
    def testReverse(self):
        s = Solution()
        self.assertEqual(321, s.reverse(123))
        self.assertEqual(-321, s.reverse(-123))
        self.assertEqual(21, s.reverse(120))

def main():
    unittest.main()

if __name__ == "__main__":
    main()
        