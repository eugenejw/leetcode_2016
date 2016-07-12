# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    #DFS solutions
    #https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
    #Solution from https://discuss.leetcode.com/topic/12241/my-recursive-solution-java
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return
        if root.left:
            root.left.next = root.right
        if root.next and root.right:
            root.right.next = root.next.left
        
        self.connect(root.left)
        self.connect(root.right)
        



"""
#My BFS iteration solution
#96ms
from collections import deque
class Solution(object):
    def connect(self, root):
        dq = deque()
        if not root:
            return 
        dq.append(root)
        while dq:
            L = len(dq)
            for i in xrange(L):
                node = dq.popleft()
                L -= 1
                if L:
                    node.next = dq[0]
                    #print "here"
                else:
                    node.next = None
                    
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
"""
