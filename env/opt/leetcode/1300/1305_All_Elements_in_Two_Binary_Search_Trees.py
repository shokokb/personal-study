# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        ret = []
        q1 = deque()
        q1.append(root1)
        if root1:
            while q1:
                node = q1.popleft()
                if node.left:
                    q1.append(node.left)
                if node.right:
                    q1.append(node.right)
                ret.append(node.val)
        if root2:
            q2 = deque()
            q2.append(root2)
            while q2:
                node = q2.popleft()
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
                ret.append(node.val)
        ret.sort()
        return ret