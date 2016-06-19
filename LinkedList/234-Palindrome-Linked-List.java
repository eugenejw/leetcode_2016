/*
https://leetcode.com/problems/palindrome-linked-list/
ref: https://leetcode.com/discuss/78152/java-easy-to-understand
 */

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public boolean isPalindrome(ListNode head) {
        //find the mid node
        ListNode s = head;
        ListNode f = head;
        ListNode p = head;
        while (f!=null && f.next!=null){
            s = s.next;
            f = f.next.next;
        }
        //reverse the 2nd half
        ListNode N = new ListNode(0);
        ListNode Terminate = N;
        while (s!=null){
            ListNode tmp = s;
            s = s.next;
            tmp.next = N;
            N = tmp;
        }
        //N is not the new head of 2nd half
        while (N!=Terminate){
            if (N.val!=p.val){
                return false;
            }
            N = N.next;
            p = p.next;
        }
        return true;
    }
}
