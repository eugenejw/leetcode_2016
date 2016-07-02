"""
https://leetcode.com/problems/odd-even-linked-list/
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
            
        s = head
        f = head.next
        s_head = head
        f_head = f
        while f and f.next:
            s.next = f.next
            s = s.next
            f.next = f.next.next
            f = f.next
        s.next = f_head
        return s_head
        
            
        