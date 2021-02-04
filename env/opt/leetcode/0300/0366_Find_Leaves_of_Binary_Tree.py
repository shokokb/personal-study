# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        ret = []
        while root:
            if root.left is None and root.right is None:
                ret.append([root.val])
                break            
            ans = []
            q = deque()
            q.append(root)
            while q:
                node = q.popleft()
                if node.left is not None:
                    if node.left.left is None and node.left.right is None:
                        ans.append(node.left.val)
                        node.left = None
                    else:
                        q.append(node.left)
                if node.right is not None:
                    if node.right.left is None and node.right.right is None:
                        ans.append(node.right.val)
                        node.right = None
                    else:
                        q.append(node.right)
            ret.append(ans)
        return ret
            
        