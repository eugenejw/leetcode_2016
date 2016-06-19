"""
https://leetcode.com/problems/valid-palindrome/
"""

#import re
#from collections import deque
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        l, r = 0, len(s)-1
        while l<r:
            while l<r and not s[l].isalnum():
                l += 1
            while l<r and not s[r].isalnum():
                r -= 1
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
                
        """
>>> timeit.timeit('import re; import string; s = "".join(ch for ch in string.printable if ch.isalnum())', number=10000)
0.20884990692138672
>>> timeit.timeit('import re; import string; s = filter(str.isalnum, string.printable)', number=10000)
0.16456985473632812
>>> timeit.timeit('import re; import string; pattern=re.compile("[^a-zA-Z0-9]"); pattern.sub("", string.printable)', number=10000)
0.16027021408081055
>>> timeit.timeit('import re; import string; s = re.sub(r"[^a-zA-Z0-9]", "", string.printable)', number=10000)
0.15453004837036133
        """
                
        """deque
        q = deque()
        s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
        print s
        if not s:
            return True
        for e in list(s):
            q.append(e)
        while len(q)>1:
            l = q.popleft()
            r = q.pop()
            if l != r:
                return False
        return True
        """
        
        
