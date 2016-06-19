"""
https://leetcode.com/problems/single-number/
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #using XOR
        res = 0
        for num in nums:
            res ^= num
        return res
        #using hashset
        '''
        d = dict()
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        for num, count in d.items():
            if count == 1:
                return num
        '''
