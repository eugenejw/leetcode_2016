#https://leetcode.com/problems/search-insert-position/

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #classic bianary search solutions
        l = 0
        r = len(nums)-1

        while l<=r:
            m = (l+r)/2
            if target < nums[m]:
                r = m - 1
            elif target > nums[m]:
                l = m + 1
            else:
                return m
        if m==l:
            return r + 1
        else:
            return l 
