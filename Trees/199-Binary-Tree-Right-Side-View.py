# Definition for a binary tree node.
# https://leetcode.com/problems/binary-tree-right-side-view/
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #right side pre-order DFS
        #60ms
        res = []
        self.dfs(root, 0, res)
        return res
        
    def dfs(self, node, lv, res):
        if not node:
            return
        if lv == len(res):
            res.append(node.val)
        self.dfs(node.right, lv+1, res)
        self.dfs(node.left, lv+1, res)
        
        
        

"""
class Solution(object):
    def rightSideView(self, root):
        #left side DFS
        #52ms
        res = []
        d = {}
        self.dfs(root, 0, res)
        for lv, val in res:
            if lv not in d:
                d[lv] = val
            else:
                d[lv] = val
        res = []
        for lv, val in d.items():
            res.append((lv, val))
        res.sort()
        return [x[1] for x in res]
        
    def dfs(self, node, lv, res):
        if not node:
            return
        res.append((lv, node.val))
        self.dfs(node.left, lv+1, res)
        self.dfs(node.right, lv+1, res)
"""        
        
        
"""
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        #BFS
        #56ms
        if not root:
            return []
        stack = deque()
        stack.append(root)
        res = []
        while stack:
            lst = []
            for _ in xrange(len(stack)):
                node = stack.popleft()
                lst.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            res.append(lst[-1])
        return res
"""
