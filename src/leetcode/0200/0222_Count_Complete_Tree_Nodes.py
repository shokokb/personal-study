# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def inorder(root:TreeNode) -> List[int]:
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []
        return len(inorder(root))
        