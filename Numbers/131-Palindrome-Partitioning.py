class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        :@link https://leetcode.com/problems/palindrome-partitioning/
        """
        res = []
        path = []
        #for pivot in xrange(len(s)):
        self.dfs(s, 0, path, res)
        return res
        
    def dfs(self, s, start, path, res):
        if start  == len(s):
            res.append(path[:])
            return
        
        for i in xrange(start+1, len(s)+1):
            curString = s[start:i]
            if self.isPalindrome(s, start, i-1):
                path.append(curString)
                self.dfs(s, i, path, res)
                path.pop()
            
    def isPalindrome(self, s, l, r):
        """helper func that checks whether the input string is palindrome
        :@return boolean
        """
        if l == r:
            return True
        while (l < r):
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
