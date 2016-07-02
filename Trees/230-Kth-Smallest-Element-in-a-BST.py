"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#follow-up solution, we can pre-store the counts on nodes to make it O(logn)
#credit,
#https://leetcode.com/discuss/43771/implemented-java-binary-search-order-iterative-recursive
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        count = self.getHeight(root.left)
        if k <= count:
            return self.kthSmallest(root.left, k)
        elif k > count + 1:
            return self.kthSmallest(root.right, k-1-count)
        else:
            return root.val
        
    def getHeight(self, node):
        if not node:
            return 0
            
        return 1 + self.getHeight(node.left) + self.getHeight(node.right)



"""
class Solution(object):
    def kthSmallest(self, root, k):
        ret = 0
        count = k
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                ret = root.val
                count -= 1
                if count == 0:
                    break
                root = root.right
        return ret
"""

"""
#Recursive Solution
#O(k) -- thus O(n)
class Solution(object):
    def __init__(self):
        self.ret = None
        self.count = None
        
    def kthSmallest(self, root, k):

        #in-order traversal
        self.count = k
        self.dfs(root)
        return self.ret
        
    def dfs(self, node):
        if not node:
            return
        if self.count == 0:
            return
        
        self.dfs(node.left)
        if self.count <= 0:
            return
        self.ret = node.val
        self.count -= 1
        self.dfs(node.right)
"""
