class Solution:
    def intToRoman(self, num: int) -> str:
        ret = ""
        hash = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
        }
        div = 1000
        while div >= 1:
            c = num // div

            b = hash[div]
            num -= c * div
            if c == 4:
                ret += b + hash[div * 5]
            elif c == 9:
                ret += b + hash[div * 10]
            elif c >= 5:
                ret += hash[div * 5]
                c -= 5
                for i in range(c):
                    ret += b
            else:
                for i in range(c):
                    ret += b

            div = div // 10

        return ret


if __name__ == "__main__":
    sol = Solution()
    print(sol.intToRoman(58))
