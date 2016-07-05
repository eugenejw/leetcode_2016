#https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
            
        node = TreeNode(0)
        m = len(nums)/2
        node.val = nums[m]
        node.left = self.sortedArrayToBST(nums[:m])
        node.right = self.sortedArrayToBST(nums[m+1:])
        
        return node


        
