# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convert(self, parent:TreeNode, preorder:List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        
        if len(preorder) == 1:
            return parent

        left = list(filter(lambda n: n < parent.val, preorder))
        right = list(filter(lambda n: n > parent.val, preorder))
        # print("tree", left, parent.val, right)
        if len(left) > 0:
            parent.left = TreeNode(left[0])
            self.convert(parent.left, left)
        if len(right) > 0:                
            parent.right = TreeNode(right[0])
            self.convert(parent.right, right)
        
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        self.convert(root, preorder)
        return root
                
        