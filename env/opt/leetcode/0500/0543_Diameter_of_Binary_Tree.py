# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1
        def depth(root:TreeNode):
            if root is None: return 0
            left = depth(root.left)
            right = depth(root.right)
            self.ans = max(self.ans, left + right + 1)
            return max(left, right) +  1
        depth(root)
        return self.ans - 1