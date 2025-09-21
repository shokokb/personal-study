# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insert(self, nums:List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0], None, None)
        mv = max(nums)
        mi = nums.index(mv)
        # print(mv, nums[:mi], nums[mi+1:])
        left = self.insert(nums[:mi])
        right = self.insert(nums[mi+1:])
        return TreeNode(mv, left, right) 

    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        return self.insert(nums) 