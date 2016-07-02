"""
https://leetcode.com/problems/maximum-product-of-word-lengths/
"""

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        #Bitwise Operations
        bits = []
        for word in words:
            tmp = 0
            for l in word:
                tmp |= (1 << (ord(l) - 96))
            bits.append(tmp)
        #print bits
        m = 0
        for i in xrange(len(words)):
            for j in xrange(i+1, len(words)):
                if bits[i]&bits[j] == 0:
                    #print 'here'
                    tmp = len(words[i])*len(words[j])
                    if tmp > m:
                        m = tmp
        return m
        
        
        #timed out solution O(n^2)
        """
        m = 0
        for i in xrange(len(words)):
            cur_s = set(words[i])
            cur_l = len(words[i])
            for j in xrange(i+1, len(words)):
                flag = False
                for letter in set(words[j]):
                    if letter in cur_s:
                        flag = True
                        break
                if flag:
                    continue
                local_max = cur_l * len(words[j])
                if local_max > m:
                    m = local_max
        return m
        """
