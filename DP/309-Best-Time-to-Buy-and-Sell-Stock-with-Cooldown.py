"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
"""
class Solution(object):
    def __init__(self):
        self.p = []
        self.s = []
        self.b = []
        
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        self.p = prices
        self.s_memo = [None] * len(self.p)
        self.b_memo = [None] * len(self.p)
        return self.sell(len(self.p)-1)
        
    def buy(self, i):
        if i <= 0:
            return -self.p[0]

        if self.b_memo[i]:
            return self.b_memo[i]
        else:
            self.b_memo[i] = max((self.sell(i-2)-self.p[i]), self.buy(i-1))
            return self.b_memo[i]
        
    def sell(self, i):
        if i <= 0:
            return 0
        if self.s_memo[i]:
            return self.s_memo[i]
        else:
            self.s_memo[i] = max((self.buy(i-1)+self.p[i]), self.sell(i-1))
            return self.s_memo[i]

        
