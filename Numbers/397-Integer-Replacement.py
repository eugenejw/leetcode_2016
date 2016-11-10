class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
	@link https://leetcode.com/problems/integer-replacement/
        @DP solution
        """
        memo = {1: 0}
        return self.opt(memo, n)
        
    def opt(self, memo, i):
        if i in memo:
            return memo[i]
        else:
            if i % 2 == 0:
                memo[i] = self.opt(memo, i/2) + 1
            else:
                left = self.opt(memo, i-1) + 1
                right = self.opt(memo, i+1) + 1
                memo[i] = min(left, right)
            return memo[i]
        
