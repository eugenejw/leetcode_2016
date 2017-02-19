class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        hash = [0] * 256
        for letter in p:
            hash[ord(letter)] += 1
        count = len(p)
        l, r = 0, 0
        while r < len(s):
            #if r pos 
            if hash[ord(s[r])] >= 1:
                count -= 1
            
            hash[ord(s[r])] -= 1
            r += 1
            
            if count == 0:
                res.append(l)
            
            if r - l == len(p):
                if hash[ord(s[l])] >= 0:
                    count += 1
                hash[ord(s[l])] += 1
                l += 1
        return res
            
