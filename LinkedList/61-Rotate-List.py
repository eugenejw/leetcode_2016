# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        newH = None
        tail = head
        len = 1
        while tail.next:
            tail = tail.next
            len += 1
        #circle it
        tail.next = head
        k = k%len
        if k:
            for _ in xrange(len-k):
                tail = tail.next
            
        newH  = tail.next
        tail.next = None

        return newH
        
