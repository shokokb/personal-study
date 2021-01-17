# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def deepestLeavesSum(self, root: TreeNode) -> int:
        max_depth = 0
        ret = 0
        
        q = deque()
        q.append((root, max_depth))
        
        while len(q) > 0:
            n, d = q.popleft()
            
            if d > max_depth:
                ret = n.val
                max_depth = d
            else:
                ret += n.val            
            #print(n.val,d, max_depth, ret)
            
            if n.left:
                q.append((n.left,d+1))
            if n.right:
                q.append((n.right,d+1))
                
        return ret