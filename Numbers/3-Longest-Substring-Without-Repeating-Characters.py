class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        MAX = 0
        res = ''
        buff = {}
        for i in xrange(len(s)):
            if s[i] not in buff:
                buff[s[i]] = i+1
                curMax = i - start + 1
                if curMax > MAX:
                    MAX = curMax
                    res = s[start: i-start+1]
            else:
                if buff[s[i]] > start:
                    start = buff[s[i]]
                    buff[s[i]] = i + 1
                    curMax = i - start + 1
                    if curMax > MAX:
                        MAX = curMax
                        res = s[start: i-start+1]
                else:
                    buff[s[i]] = i+1
                    curMax = i - start + 1
                    if curMax > MAX:
                        MAX = curMax
                        res = s[start: i-start+1]
        return MAX
                
                
                
