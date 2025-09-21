# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sumv: int) -> List[List[int]]:
        if not root:
            return []
        
        paths = []
        stack = [(root, [root.val])]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                if sum(path) == sumv:
                    paths.append(path)
            if node.left:
                p = path.copy()
                p.append(node.left.val)
                stack.append((node.left, p))
            if node.right:
                p = path.copy()
                p.append(node.right.val)
                stack.append((node.right, p))
        return paths