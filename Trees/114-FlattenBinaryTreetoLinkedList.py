# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    '''
    @link: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
    @summary: stack solution
    '''
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        stack = []
        while root:
            if root.left:
                root.right, root.left = root.left, root.right
                if root.left:
                    stack.append(root.left)
                    root.left = None
            if not root.right:
                if stack:
                    root.right = stack.pop()
                else:
                    root.right = None
            root = root.right
            

        
        
        
    
        
