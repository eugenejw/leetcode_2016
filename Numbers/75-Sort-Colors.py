class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        :https://leetcode.com/problems/sort-colors/
        """
        i = 0
        k = len(nums)-1
        j = 0 #first one's pos
        while i <= k and j <= k:
            #print "i, j are {}, {}".format(i, j)
            if nums[i] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[i] == 2:
                nums[i], nums[k]  = nums[k], nums[i]
                k -= 1
                if j == i:
                    i -= 1
                    j -= 1
                    if j < 0:
                        j = 0
                else:
                    i -= 1
                if i <0:
                    i = 0
                
            else:
                i += 1
        
        
        
        """
        #One pass, solution I
        n0, n1, n2 = -1, -1, -1
        for num in nums:
            if num == 0:
                n0 += 1
                n1 += 1
                n2 += 1
                nums[n2] = 2
                nums[n1] = 1
                nums[n0] = 0
            elif num == 1:
                n1 += 1
                n2 += 1
                nums[n2] = 2
                nums[n1] = 1
            elif num == 2:
                n2 += 1
                nums[n2] = 2
        """
                
        
        """
        #two pass bucket sort
        NUMS = 3
        bucket = [0] * NUMS
        res = []
        for num in nums:
            bucket[num] += 1
        i = 0
        for j in xrange(NUMS):
            while bucket[j]:
                nums[i] = j
                i += 1
                bucket[j] -= 1
        """

            
            
