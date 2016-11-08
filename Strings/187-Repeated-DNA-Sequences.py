class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
	@algorithm using KMP, O(n^2), using bit map will have much greater efficiency
        """
        res = []
        if len(s) < 10:
            return res
        record = {}
        for i in xrange(len(s)):
            if i+10 <= len(s):
                pattern = s[i:i+10]
                if record.get(pattern, None) and record[pattern] >= 2:
                    continue
                #print 'pattern: {}'.format(pattern)
                KMPArray = self.buildKMPArray(pattern)
                if self.searchPattern(s, i, pattern, KMPArray):
                    if pattern in record:
                        record[pattern] += 1
                    else:
                        record[pattern] = 1
                    if record.get(pattern, None) and record[pattern] == 2:
                        res.append(pattern)
            else:
                #print 'breaking'
                break
        return res
            
    def buildKMPArray(self, pattern):
        '''return list'''
        ret = [0] * len(pattern)
        j = 0
        for i in xrange(1, len(pattern)):
            while j > 0 and pattern[i] != pattern[j]:
                j = ret[j-1]
            if pattern[i] == pattern[ret[j]]:
                j += 1
            #print i
            ret[i] = j 
        #print ret
        return ret
        
    
    def searchPattern(self, s, start, pattern, KMPArray):
        '''if found return True'''
        if start >= len(s):
            return False
        j = 0
        for i in xrange(start, len(s)):
            #print 'i: {}; string: {}'.format(i, s[i])
            while j > 0 and s[i] != pattern[j]:
                j = KMPArray[j-1]
                #print 'not match, j: {}'.format(j)
            if s[i] == pattern[j]:
                #print 'matched, i:{} j:{} string{}'.format(i, j, s[i])
                j += 1
                if j == len(pattern):
                    return True

        return False
                    

                    
        
        
