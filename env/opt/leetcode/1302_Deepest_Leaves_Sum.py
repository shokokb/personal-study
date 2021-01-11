# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def deepestLeavesSum(self, root: TreeNode) -> int:
        def depth(tree:TreeNode) -> int:
            if not tree:
                return 0
            return max(depth(tree.left), depth(tree.right)) + 1

        ret = 0
        
        tree_depth = depth(root)
        # print("depth", tree_depth)
        
        # Breath First Search       
        q = deque()
        qd = deque()

        q.append(root)
        qd.append(1)

        while len(q) > 0:
            n = q.pop()
            d = qd.pop()
            
            if d == tree_depth:
                ret += n.val
                # print(n.val, d)
            
            if n.left:
                q.append(n.left)
                qd.append(d + 1)
            if n.right:
                q.append(n.right)
                qd.append(d + 1)

        return ret
        