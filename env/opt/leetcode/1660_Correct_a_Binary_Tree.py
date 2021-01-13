# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:        
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        seen = [root]
        incorrect_num = 0
        
        q = deque()
        q.append((root, None, 0))
        while len(q) > 0:
            p, parent, side = q.popleft()
            if p.left:
                q.append((p.left, p, 0))
                seen.append(p.left)
            if p.right:
                if p.right in seen:
                    incorrect_num = p.val
                    if side == 0:
                        parent.left = None
                    else:
                        parent.right = None
                    break
                q.append((p.right, p, 1))
                seen.append(p.right)
                
        return root
            