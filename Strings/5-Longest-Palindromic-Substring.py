from collections import namedtuple
resultConstruct = namedtuple('resultConstruct', 'low maxLen')

class Solution(object):
    def __init__(self):
        self.maxLen = 0
        self.low = 0
        
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        for i in xrange(len(s)):
            self.extend(i, i, s)
            self.extend(i, i+1, s)
        return s[self.low : self.low+self.maxLen]
            
    def extend(self, j, k, s):
        while j>=0 and k<len(s) and s[j]==s[k]:
            j -= 1
            k += 1
        if self.maxLen < k-j-1:
            self.maxLen = k-j-1
            self.low = j+1
        
        
