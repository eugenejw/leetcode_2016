class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        @link https://leetcode.com/problems/summary-ranges/
        """
        res = []
        i = 0
        while i != len(nums):
            tmp = []
            while i+1<len(nums) and nums[i]+1==nums[i+1]:
                tmp.append(nums[i])
                i += 1
            tmp.append(nums[i])
            i += 1
            res.append(tmp[:])
        ret = [] 
        for tmp in res:
            if len(tmp) == 1:
                summary = '{}'.format(tmp[0])
            else:
                summary = '{}->{}'.format(tmp[0], tmp[-1])
            ret.append(summary)
        return ret
            
                
            
        
