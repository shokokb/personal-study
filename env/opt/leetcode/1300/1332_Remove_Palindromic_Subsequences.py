class Solution:
    def removePalindromeSub(self, s: str) -> int:
        def is_palindrome(s:str) -> bool:
            left = 0
            right = len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        if s == "":
            return 0
        if is_palindrome(s):
            return 1
        return 2