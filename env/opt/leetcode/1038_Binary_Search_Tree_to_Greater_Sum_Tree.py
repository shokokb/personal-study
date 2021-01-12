# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum_value = 0

    def dfs(self, node:TreeNode):
        if not node:
            return
        self.dfs(node.right)
        self.sum_value += node.val
        node.val = self.sum_value
        self.dfs(node.left)
        return
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.dfs(root)
        return root