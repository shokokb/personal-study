class Solution:
    def paths(self, start:int, graph:List[List[int]]) -> List[List[int]]:
        ret = []
        if start == len(graph) - 1:
            return [[start]]
        for np in graph[start]:
            next_paths = self.paths(np, graph)
            for next_path in next_paths:
                path = [start]
                path.extend(next_path)
                ret.append(path)
        return ret
    
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        return self.paths(0, graph)
