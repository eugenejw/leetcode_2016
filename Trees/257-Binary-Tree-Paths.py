'''
https://leetcode.com/problems/binary-tree-paths/

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def __init__(self):
        self.res = []
    
    def binaryTreePaths(self, root):
        #BFS stack
        if not root:
            return []
        stack = deque()
        stack.append((root, []))
        while stack:
            node, path = stack.popleft()
            if not node.left and not node.right:
                path += [node.val]
                self.res.append("->".join(map(str, path)))

            if node.left:
                stack.append((node.left, path+[node.val]))
            if node.right:
                stack.append((node.right, path+[node.val]))
        return self.res
            
    
    """    
    def binaryTreePaths(self, root):
        #DFS STACK
        if not root:
            return []
        stack = []
        stack.append((root, []))
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                path += [node.val]
                self.res.append("->".join(map(str, path)))
            if node.right:
                stack.append((node.right, path+[node.val]))
            if node.left:
                stack.append((node.left, path+[node.val]))
        return self.res
    """
            
    """DFS RECURSIVE
    def __init__(self):
        self.res = set()
        
    def binaryTreePaths(self, root):
        self.dfs(root, [])
        return list(self.res)
        
    def dfs(self, node, path):
        if not node:
            return
        if not node.left and not node.right:
            path += [node.val]
            tmp = "->".join(map(str, path))
            if tmp not in self.res:
                self.res.add(tmp)
            return 
        self.dfs(node.left, path+[node.val])
        self.dfs(node.right, path+[node.val])
    """
        
