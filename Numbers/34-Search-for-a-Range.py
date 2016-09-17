class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        :@solution two runs of binary search
        :@see https://leetcode.com/problems/search-for-a-range/
        """
        left, right = -1, -1
        #find left
        l, r = 0, len(nums)-1
        while l<=r:
            m = (l + r) / 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                left = m
                if m != 0 and nums[m-1] == target:
                    r = m - 1
                else:
                    break
        #find right
        l, r = 0, len(nums)-1
        while l<=r:
            m = (l + r) / 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                right = m
                if m != len(nums)-1 and nums[m+1] == target:
                    l = m + 1
                else:
                    break  

        return [left, right]

                
