class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in xrange(32):
            res <<= 1
            res |= (n>>i)&1
        return res
