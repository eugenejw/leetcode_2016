class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        :@see https://leetcode.com/problems/anagrams/
        """
        resInDict = dict()
        for aStr in strs:
            keyTuple = self.helper(list(aStr))
            #print 'keyTuple is {}'.format(keyTuple)
            if keyTuple not in resInDict:
                resInDict[keyTuple] = [aStr]
            else:
                resInDict[keyTuple].append(aStr)
        #print "resInDict is {}".format(resInDict)
        return [resInDict[keyTuple] for keyTuple in resInDict]
            
    def helper(self, aList):
        #still O(nlogn), which is slightly better than sorting the aStr directly
        count = [0]* 26

        for letter in aList:
            count[ord(letter)-97] += 1
        return tuple(count)
        
