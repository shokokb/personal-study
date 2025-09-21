# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        ret = []
        q = deque()
        q.append(root)
        while q:
            p = q.popleft()
            if p.left:
                q.append(p.left)
                if not p.right: ret.append(p.left.val)
            if p.right:
                q.append(p.right)
                if not p.left: ret.append(p.right.val)
        return ret
                