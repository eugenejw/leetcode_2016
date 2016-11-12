class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        count = 0
        for byte in data:
            if count == 0:
                if byte >> 3 == 0b11110:
                    count = 3
                elif byte >> 4 == 0b1110:
                    count = 2
                elif byte >> 5 == 0b110:
                    count = 1
                elif byte >> 7 ==0b0:
                    count = 0
                else:
                    #print count
                    return False
            else:
                #print 'here'
                if byte >> 6 != 0b10:
                    return False
                count -= 1
        return count == 0
        
