class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        @link https://leetcode.com/problems/word-break/
        """
        memo = [False] * (len(s) + 1)
        memo[0] = True
        for i in xrange(1, len(s)+1):
            for j in xrange(i-1, -1, -1):
                #print j
                if memo[j]:
                    if s[j:i] in wordDict:
                        memo[i] = True
                        break
        #print memo
        return memo[-1]
                        
                    
                
            
