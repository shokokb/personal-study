# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__ (self):
        self.fbts = dict() 
        
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N == 0:
            return []
        if N == 1:
            return [TreeNode(0)]
        roots = []
        for n in range(1, N, 2):
            lefts = None
            try:
                lefts = self.fbts[n]
            except:
                lefts = self.allPossibleFBT(n)
                self.fbts[n] = lefts
            rights = None
            try:
                rights = self.fbts[N - 1 -n]
            except:
                rights = self.allPossibleFBT(N - 1 -n)
                self.fbts[N - 1 -n] = rights

            for left in lefts:
                for right in rights:
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    roots.append(root)
        return roots