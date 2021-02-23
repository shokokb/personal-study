class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if len(trust) < N - 1:
            return -1
        trust_score = [0 for _ in range(N + 1)]

        for a, b in trust:
            trust_score[a] -= 1
            trust_score[b] += 1
            
        for i in range(1, N + 1):
            if trust_score[i] == N - 1:
                return i
        return -1