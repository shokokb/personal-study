class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if ord(word[0]) >= ord('a'):
            # 最初が小文字
            if len(word) > 1:
                for w in word[1:]:
                    if ord(w) < ord('a'):
                        return False
                return True
        else:
            # 最初が大文字
            if len(word) >= 3:
                if ord(word[1]) < ord('a'):
                    # 2文字目が大文字
                    # そのあとに大文字が続かなければFalse
                    for w in word[2:]:
                        if ord(w) >= ord('a'):
                            return False
                else:
                    # 2文字目が小文字
                    # そのあとに小文字が続かなければFalse
                    for w in word[2:]:
                        if ord(w) < ord('a'):
                            return False
        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.detectCapitalUse("ffffffffffffffffffffF"))
