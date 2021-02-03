# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        head = root
        while True:
            if head is None:
                return None
            if val == head.val:
                return head
            if val < head.val:
                head = head.left
            else:
                head = head.right