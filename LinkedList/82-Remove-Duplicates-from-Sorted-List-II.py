i# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        @link https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
        """
        dummy = ListNode(0)
        dummy.next = head
        prev, cur = dummy, head
        while cur:
            nxt = cur.next
            duplicated = False
            while nxt and nxt.val == cur.val:
                duplicated = True
                nxt = nxt.next
            if duplicated:
                prev.next = nxt
                cur = nxt
            else:
                cur = cur.next
                prev = prev.next
        return dummy.next
            
        
