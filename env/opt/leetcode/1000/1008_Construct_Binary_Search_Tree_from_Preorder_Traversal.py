# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convert(self, l:List[TreeNode]) -> TreeNode:
        if len(l) == 0:
            return None
        
        if len(l) == 1:
            return l[0]
        
        parent = l[0]
        left = list(filter(lambda n: n.val < parent.val, l))
        right = list(filter(lambda n: n.val > parent.val, l))
        if len(left) > 0:
            parent.left = left[0]
            self.convert(left)
        if len(right) > 0:                
            parent.right = right[0]
            self.convert(right)
        
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        l = [TreeNode(v) for v in preorder]
        self.convert(l)
        return l[0]