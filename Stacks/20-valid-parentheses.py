"""
https://leetcode.com/problems/valid-parentheses/
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {")": "(", "]": "[", "}": "{"}
        stack = []
        s = list(s)
        for e in s:
            if e in ("{", "(", "["):
                stack.append(e)
            else:
                if not stack:
                    return False
                if d[e] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        else:
            return True
