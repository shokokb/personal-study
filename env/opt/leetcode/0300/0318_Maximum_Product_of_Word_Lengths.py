class Solution:
    # TimeComplexty O(n^2)
    def maxProduct(self, words: List[str]) -> int:
        def get_bit_mask (s) -> int:
            bit_number = lambda ch: ord(ch) - ord('a')
            bit_mask = 0
            for c in s:
                bit_mask |= 1 << bit_number(c) 
            return bit_mask
                        
        n = len(words)
        max_prod = 0

        # O(n)
        bit_masks = [get_bit_mask(words[i]) for i in range(n)]
        # O(n^2)
        for i in range(n):
            for j in range(i + 1, n):
                if bit_masks[i] & bit_masks[j] == 0:
                    max_prod = max(max_prod, len(words[i]) * len(words[j]))
        return max_prod