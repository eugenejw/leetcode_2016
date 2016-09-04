# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    '''
    @see https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
    '''
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(root, res, 0)
        return res
        
    def dfs(self, node, res, level):
        if not node:
            return
        if len(res) <= level:
            res.append([])
            
        if level%2 == 0:
            res[level].append(node.val)
        else:
            res[level].insert(0, node.val)
            
        self.dfs(node.left, res, level+1)
        self.dfs(node.right, res, level+1)
    #48ms
    #beats 88%-97%
    #DFS via recursion
        
'''
class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        res = []
        stack = deque()
        stack.append(root)
        while stack:
            thisLevel = []
            for _ in xrange(len(stack)):
                node = stack.popleft()
                thisLevel.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            res.append(thisLevel)
            
        for i in xrange(len(res)):
            if i%2 != 0:
                res[i].reverse()
        return res
        
        #45ms
        #beats 98%-100%
        #BFS via stack'''
