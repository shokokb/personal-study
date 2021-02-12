# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder (root):
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []
        q1 = inorder(root1)
        q2 = inorder(root2)
        return sorted(q1 + q2)