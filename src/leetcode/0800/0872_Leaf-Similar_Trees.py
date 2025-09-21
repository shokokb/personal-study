# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(root:TreeNode) -> List[int]:
            if root is None:
                return []
            if root.left is None and root.right is None:
                return [ root.val ]
            return dfs(root.left) + dfs(root.right)
        return dfs(root1) == dfs(root2)
