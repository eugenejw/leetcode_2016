'''
https://leetcode.com/problems/remove-linked-list-elements/
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
            
        p = head
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return head if head.val!=val else head.next
            
        
        """Solution using prev
        p = head
        d = ListNode(0)
        d.next = head
        prev = d
        while p:
            if p.val == val:
                prev.next = p.next
                p = p.next
            else:
                prev = p
                p = p.next
        return d.next
        ""



XCxc"
