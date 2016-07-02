"""
https://leetcode.com/problems/binary-tree-preorder-traversal/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution(object):
    #DFS
    def preorderTraversal(self, root):
        if not root:
            return []
        res = []
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res


class Solution(object):
    #DFS without helper
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        res.append(root.val)
        res += self.preorderTraversal(root.left)
        res += self.preorderTraversal(root.right)
        return res
        

#recursive solutions
class Solution(object):
    #Dfs with helper
    def __init__(self):
        self.res = []
    def preorderTraversal(self, root):

        self.dfs(root)
        return self.res
        
    def dfs(self, node):
        if not node:
            return
        self.res.append(node.val)
        self.dfs(node.left)
        self.dfs(node.right)
        
"""
