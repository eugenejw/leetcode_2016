# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        @see https://leetcode.com/problems/insertion-sort-list/
        @see https://discuss.leetcode.com/topic/8570/an-easy-and-clear-way-to-sort-o-1-space/7
        """
        dummy = ListNode(0)
        cur = head
        prev = dummy
        while cur:
            if prev.next and prev.next.val > cur.val:
                #only reset the prev back to dummy when cur is less than prev.next.val
                prev = dummy
            while prev.next:
                if prev.next.val <= cur.val:
                    prev = prev.next
                else:
                    break
            nxt = cur.next
            cur.next = prev.next
            prev.next = cur
            cur = nxt
            
        return dummy.next
