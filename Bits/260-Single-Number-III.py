"""
https://leetcode.com/problems/single-number-iii/
ref: https://leetcode.com/discuss/70790/easy-python-o-n-o-1-solution
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #using bit operations
        xor = 0
        for num in nums:
            xor ^= num
        
        #to find the last 1 in xor
        mask = 1
        while xor&mask==0:
            mask = mask<<1
        a, b = 0, 0
        for num in nums:
            if num&mask:
                a ^= num
            else:
                b ^= num
        return [a, b]
                
        
        """
        #using sort
        #O(nlogn) time and O(n) space
        nums.sort()
        i = 0
        res = []
        while i < len(nums)-1:
            if nums[i] != nums[i+1]:
                res.append(nums[i])
                if len(res) == 2:
                    return res
                i += 1
            else:
                i += 2
        res += [nums[-1]]
        return res
        """
            
        #using hash table
        #O(n) time complexity and O(n/2) space complexity
        #or could use set.add(x) and set.remove(x), maybe better
        """
        d = dict()
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        res = []
        for num, count in d.items():
            if count == 1:
                res.append(num)
        return res
        """
