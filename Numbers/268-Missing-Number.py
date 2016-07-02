"""
https://leetcode.com/problems/missing-number/
"""
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #using binary search O(nlogn)
        nums.sort()
        l = 0
        r = len(nums)-1
        while l<r:
            m = (l+r)/2
            if nums[m]==m:
                l = m+1
            else:
                r = m-1
        if nums[l] != l:
            return l
        else:
            return l+1
        
        """
        #Using XOR O(n)
        res = 0
        for i in xrange(len(nums)):
            res ^= i
            res ^= nums[i]
        res ^= len(nums)
        return res
        """
        
        """
        #Using hash set O(n)
        s = set()
        for i in xrange(len(nums)+1):
            s.add(i)
        for num in nums:
            s.remove(num)
        return list(s)[0]
        """
        
