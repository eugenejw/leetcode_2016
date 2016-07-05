"""
https://leetcode.com/problems/generate-parentheses/
"""

"""
#Better DFS
class Solution(object):
    def __init__(self):
        self.res = []
        
    def generateParenthesis(self, n):
        self.dfs('', n, n)
        return self.res
        
    def dfs(self, path, left, right):
        if left > right:
            return        
        if right==0 and left==0:
            self.res.append(path)
            return
            
        if left > 0:
            self.dfs(path+'(', left-1, right)
        if right > 0:
            self.dfs(path+')', left, right-1)
            
"""


    
        
        

#Following DFS accepted, but involves level
class Solution(object):
    def __init__(self):
        self._2n = None
        self.res = []
        self.n = None
                
    def generateParenthesis(self, n):

        self._2n = n*2
        self.n = n
        self.dfs(0, '', 0)
        return self.res
        
    def dfs(self, lv, path, val):
        if val < 0 or val>self.n:
            return
        if lv == self._2n:
            if val == 0:
                self.res.append(path)
            return 
        self.dfs(lv+1, path+'(', val+1)
        self.dfs(lv+1, path+')', val-1)
        
