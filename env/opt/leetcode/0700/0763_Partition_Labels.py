class Solution:
    def partition(self, S:str) -> str:
        for i, c in enumerate(S):
            s1 = set(S[0:i+1])
            s2 = set(S[i+1:])
            if len(s1 & s2) == 0:
                return S[0:i+1]
        return ""

    def partitionLabels(self, S: str) -> List[int]:
        ret = []
        index = 0
        while index < len(S):
            s = self.partition(S[index:])
            index += len(s)
            ret.append(len(s))
        return ret