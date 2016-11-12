import itertools
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str†
        :rtype: bool
        @link https://leetcode.com/problems/additive-number/
        """
        for i, j in itertools.combinations(range(1, len(num)), 2):
            a, b = num[0:i], num[i:j]
            if b != str(int(b)) or a != str(int(a)):
                continue
            while j < len(num):
                c = str(int(a) + int(b))
                if not num.startswith(c, j):
                    break
                else:
                    j += len(c)
                    a, b = b, c
            if j == len(num):
                return True
        return False
                    
                
        
        
"""
DFS solution does not early terminate 
        path = []
        res = []
        self.dfs(0, num, path, res)
        #print res
        ret = []
        for tmp in res:
            ret.append(self.AdditiveNumberCheck(tmp))
        return any(ret)
        
    def dfs(self, start, num, path, res):
        if start == len(num):
            res.append(path[:])
            return 
        for i in xrange(start, len(num)):
            if len(num[start:i+1])>1 and num[start] == '0':
                return
            else:
                self.dfs(i+1, num, path+[num[start:i+1]], res)
            
        
    def AdditiveNumberCheck(self, num):
        num = map(int, num)
        if len(num) < 3:
            return False
        flag = True
        for i in xrange(len(num)-2):
            if num[i] + num[i+1] != num[i+2]:
                flag = False
                break
        return flag
"""
            
            
        
