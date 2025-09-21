class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ans = 0
        rule = { "type":0, "color":1, "name":2 }
        for item in items:
            if item[rule[ruleKey]] == ruleValue:
                ans += 1
            # print(item[rule[ruleKey]])
        return ans