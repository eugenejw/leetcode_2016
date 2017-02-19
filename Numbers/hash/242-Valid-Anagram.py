class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        bucket = [0] * 26
        for i in xrange(len(s)):
            bucket[ord(s[i])-97] += 1
        for j in xrange(len(t)):
            bucket[ord(t[j])-97] -= 1
        return not any(bucket)
        
