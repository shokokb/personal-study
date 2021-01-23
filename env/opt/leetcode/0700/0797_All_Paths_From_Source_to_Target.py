class Solution:
    def __init__(self):
        self._paths = defaultdict(lambda: None)
        
    def paths(self, start:int, graph:List[List[int]]) -> List[List[int]]:
        ret = []
        if start == len(graph) - 1:
            return [[start]]
        for np in graph[start]:
            next_paths = self._paths[np]
            if self._paths[np] is None:
                self._paths[np] = next_paths = self.paths(np, graph)                
            for next_path in next_paths:
                path = [start]
                path.extend(next_path)
                ret.append(path)
        return ret
    
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        return self.paths(0, graph)
