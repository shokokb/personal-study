# coding : UTF-8
import unittest
class Solution:

    def romanToInt(self, s: str) -> int:
        ret = 0
        l = list(s)
        char_to_value = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100, 
            'D': 500,
            'M': 1000
        }
        place_before = {
            'I': '',
            'V': 'I',
            'X': 'I',
            'L': 'X',
            'C': 'X', 
            'D': 'C',
            'M': 'C'
        }
        while l:
            c = l.pop()
            ret += char_to_value[c]
            if l and l[-1] == place_before[c]:
                c = l.pop()
                ret -= char_to_value[c]

        return ret

class TestSolution(unittest.TestCase):
    def testRomanToInt(self):
        s = Solution()
        self.assertEqual(3,     s.romanToInt("III"))
        self.assertEqual(58,    s.romanToInt("LVIII"))
        self.assertEqual(1994,  s.romanToInt("MCMXCIV"))

def main():
    unittest.main()

if __name__ == "__main__":
    main()