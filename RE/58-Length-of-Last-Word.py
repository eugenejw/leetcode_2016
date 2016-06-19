class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        #using split
        s = s.strip()
        if not s:
            return 0
        lst = s.split(' ')
        print lst
        return len(lst[-1])
        
        
        '''
        #Using Python String Funcs
        s = s.strip()
        lastIndex = s.rfind(' ')+1
        print lastIndex-1
        return len(s)-lastIndex
