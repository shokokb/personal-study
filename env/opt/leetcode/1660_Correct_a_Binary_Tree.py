# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:        
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        seen = {root}
        incorrect_num = 0
        left, right = 0, 1
        
        q = deque()
        q.append((root, None, left))
        while len(q) > 0:
            p, parent, side = q.popleft()
            if p.left:
                q.append((p.left, p, left))
                seen.add(p.left)
            if p.right:
                if p.right in seen:
                    incorrect_num = p.val
                    if side == left:
                        parent.left = None
                    else:
                        parent.right = None
                    break
                q.append((p.right, p, right))
                seen.add(p.right)
                
        return root
            