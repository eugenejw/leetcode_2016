"""
https://leetcode.com/problems/single-number-ii/
https://en.wikipedia.org/wiki/Two%27s_complementXC
"""

#import heapq
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #A general way of bitwiuse operations
        #https://discuss.leetcode.com/topic/23584/a-general-c-solution-for-these-type-problems/2
        bits = [0] * 32
        for num in nums:
            for i in xrange(31, -1, -1):
                if not num:
                    break
                bits[i] += num & 1  #to check whether this bit position contaains '1'
                num >>= 1
        #print bits
        res = 0
        for i in xrange(31, -1, -1):
            val = bits[i]%3
            if val:
                res += 1<<(31-i)
        #[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] is -1, but
        #in Python the range is [-2^63, 2^63-1], so the result should be res - (1<<32)
        return res if res < (1 << 31) else res - (1 << 32)
                
        
        """
        #priority queue
        pq = []
        d = dict()
        for num in nums:
            if num not in d:
                d[num] = [1, num]
            else:
                d[num][0] += 1
        for ele in d.values():
            heapq.heappush(pq, ele)
        res = heapq.heappop(pq)
        return res[1]
        """
        
        
        """
        #bucket sort
        d = dict()
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        #lst = [[] for i in xrange(len(nums))]
        for num, count in d.items():
            if count == 1:
                return num
        """
            
        
