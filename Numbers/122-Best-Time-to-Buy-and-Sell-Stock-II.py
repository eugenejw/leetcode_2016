"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
"""

#greedy way
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        p = prices
        i = 0
        L = len(prices)
        res = 0
        while i<L-1:
            local_min = None
            local_max = None
            
            #find local min
            while (i < L-1) and (p[i] >= p[i+1]):
                i += 1
            local_min = p[i]
            
            #find local max
            while (i < L-1) and (p[i] <= p[i+1]):
                i += 1
            if i<L:
                local_max = p[i]
            i += 1
            if local_max != local_min:
                res += (local_max - local_min)
            
        return res
