"""
https://leetcode.com/problems/count-primes/
"""

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 0
        A = [True]*(n+1)
        A[0] = A[1] = False
        for i in xrange(2, n):
            base = i*i
            if base >= n:
                break
            if A[i]:
                j = 0
                while base+j<n:
                    A[base+j] = False
                    j += i
        count = 0
        for i in xrange(n):
            if A[i]:
                count += 1
        return count
            
