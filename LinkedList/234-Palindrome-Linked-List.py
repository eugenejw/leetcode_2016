# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #find the mid node
        s = f = head
        while f and f.next:
            s = s.next
            f = f.next.next
        #reverse the 2nd half
        N = None
        while s:
            tmp = s
            s = s.next
            tmp.next = N
            N = tmp
        #N is now the new head of the 2nd 
        p = head
        while N:
            if N.val != p.val:
                return False
            N = N.next
            p = p.next
        return True
        
