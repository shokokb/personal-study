class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = dict()
        d["1"] = []
        d["2"] = ["a", "b", "c"]
        d["3"] = ["d", "e", "f"]
        d["4"] = ["g", "h", "i"]
        d["5"] = ["j", "k", "l"]
        d["6"] = ["m", "n", "o"]
        d["7"] = ["p", "q", "r", "s"]
        d["8"] = ["t", "u", "v"]
        d["9"] = ["w", "x", "y", "z"]
                
        def dfs (l: List[str], digits:str) -> List[str]:
            if len(digits) == 0:            
                return l
            if len(l) == 0:
                return dfs(d[digits[0]], digits[1:])
            ans = []
            for pre in l:
                for cur in d[digits[0]]:
                    ans.append(pre + cur)
            return dfs(ans, digits[1:])
        
        return dfs([], digits)