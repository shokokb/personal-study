class TreeNode:
    def __init__(self, value:int):
        self.value = value
        self.children = []
class Solution:
    def dfs(self, node) -> List[int]:
        if node is None:
            return []
        ret = [node.value]
        for n in node.children:
            ret.extend(self.dfs(n))
        return ret
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        d = dict()
        for id in pid:
            d[id] = TreeNode(id)
        for i, id in enumerate(pid):
            if ppid[i] != 0:
                d[ppid[i]].children.append(d[id])         
        return self.dfs(d[kill])