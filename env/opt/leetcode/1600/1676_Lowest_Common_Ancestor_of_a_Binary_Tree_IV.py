# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':        
        
        def dfs(root: 'TreeNode') -> 'List[TreeNode]':
            children = []
            if root.left:
                children.append(root.left)
                children.extend(dfs(root.left))
            if root.right:
                children.append(root.right)
                children.extend(dfs(root.right))
            return children
        
        if len(nodes) == 1:
            return nodes[0]
        
        children = dfs(root)
        # print(children)
        if set(children) == set(nodes):
            return root
        
        if root in nodes:
            return root
        
        if root.left:
            left = self.lowestCommonAncestor(root.left, nodes)
            if left:
                return left
        if root.right:
            right = self.lowestCommonAncestor(root.right, nodes)
            if right:
                return right        
        
        return None
    