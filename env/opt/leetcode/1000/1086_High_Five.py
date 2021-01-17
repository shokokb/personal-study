class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        ret = []
        scores = dict()
        
        for item in items:
            scores[item[0]] = list()
            
        for item in items:
            scores[item[0]].append(item[1])
                        
        id_list = sorted(list(scores.keys()))
        for i in id_list:
            scores[i] = sorted(scores[i])
            ret.append([i, sum(scores[i][-5:]) // 5])
            
        return ret
        