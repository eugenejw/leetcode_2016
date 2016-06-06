"""
https://leetcode.com/problems/minimum-depth-of-binary-tree/
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.lv = None
        
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        """https://leetcode.com/discuss/76318/very-easy-with-recursion-1ms-java-solution"""
        if not root:
            return 0
        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right))+1
        else:
            return max(self.minDepth(root.left), self.minDepth(root.right))+1
        
        """DFS Stack
        if not root:
            return 0
        s = []
        s.append((root, 1))
        while s:
            node, lv = s.pop()
            if self.lv and lv >= self.lv:
                continue
                
            if not node.left and not node.right:
                if not self.lv:
                    self.lv = lv
                else:
                    if lv < self.lv:
                        self.lv = lv
            if node.right:
                s.append((node.right, lv+1))
            if node.left:
                s.append((node.left, lv+1))
        return self.lv
        """
        
        

        
