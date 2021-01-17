# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sumv: int) -> bool:
        if not root:
            return False
        
        # (node:TreeNode, path:List[int])
        paths = []
        stack = [(root, [root.val])]
        while stack:
            node, path = stack.pop()
            if node.left is None and node.right is None:
                # Leaf
                if sum(path) == sumv:
                    return True
            if node.left:
                path_copy = path.copy()
                path_copy.append(node.left.val)
                stack.append((node.left, path_copy))
            if node.right:
                path_copy = path.copy()
                path_copy.append(node.right.val)
                stack.append((node.right, path_copy))

        return False