import sys
MAX = sys.maxint
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        @algorithm, sliding window O(n)
        @link https://leetcode.com/problems/minimum-size-subarray-sum/
        """
        sum = 0
        start = 0
        minLen = MAX
        for i in xrange(len(nums)):
            sum += nums[i]
            while  sum >= s:
                minLen = min(minLen, i-start+1)
                sum = sum - nums[start]
                start += 1
        return 0 if minLen==MAX else minLen
                
        
        
        
        
