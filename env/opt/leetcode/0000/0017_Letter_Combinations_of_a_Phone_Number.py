class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = dict()
        d["2"] = ["a", "b", "c"]
        d["3"] = ["d", "e", "f"]
        d["4"] = ["g", "h", "i"]
        d["5"] = ["j", "k", "l"]
        d["6"] = ["m", "n", "o"]
        d["7"] = ["p", "q", "r", "s"]
        d["8"] = ["t", "u", "v"]
        d["9"] = ["w", "x", "y", "z"]
                
        output = []
        def backtrack (combination: str, next_digits:str):
            if len(next_digits) == 0:            
                output.append(combination)
            else:
                for letter in d[next_digits[0]]:
                    backtrack(combination + letter, next_digits[1:])
        if digits:
            backtrack("", digits)
        return output