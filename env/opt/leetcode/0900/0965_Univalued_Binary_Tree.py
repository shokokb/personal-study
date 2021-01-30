# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        num = root.val
        queue = deque()
        queue.append(root)
        while queue:
            n = queue.popleft()
            if n.val != num:
                return False
            if n.left is not None:
                queue.append(n.left)
            if n.right is not None:
                queue.append(n.right)
        return True