class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def no_common_letters(s1, s2) -> bool:
            for c1 in s1:
                for c2 in s2:
                    if c1 == c2:
                        return False
            return True
            
        n = len(words)
        max_prod = 0
        for i in range(n):
            for j in range(i + 1, n):
                if no_common_letters(words[i], words[j]):
                    max_prod = max(max_prod, len(words[i]) * len(words[j]))
        return max_prod