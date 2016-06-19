"""
https://leetcode.com/problems/min-stack/
Linked list solution -- https://leetcode.com/discuss/63482/solution-using-linked-list-clean-self-explanatory-efficient
"""

class Node(object):
    def __init__(self, x, y):
        self.val = x
        self.minval = y
        self.next = None

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.head = None
        self.cur = None
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.head:
            self.head = Node(x, x)
        else:
            self.tmp = Node(x, min(x, self.head.minval))
            self.tmp.next = self.head
            self.head = self.tmp
        

    def pop(self):
        """
        :rtype: void
        """
        if self.head:
            self.head = self.head.next

    def top(self):
        """
        :rtype: int
        """
        return self.head.val if self.head else None
        

    def getMin(self):
        """
        :rtype: int
        """
        
        return self.head.minval if self.head else None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
