"""
https://leetcode.com/problems/combination-sum-iii/
"""

class Solution(object):
    def __init__(self):
        self.n = 0
        self.k = 0
        self.res = []
        
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.n = n
        self.k = k
        #uncomment below to get a backtracking DFS 
        #which is a more concise way of doing things
        res = []
        path = []
        self.dfs(1, path, res)
        return res
    
    def dfs(self, start, path, res):
        if len(path) == self.k:
            if sum(path) == self.n:
                res.append(path[:])
            return
        if start > 9:
            return 
        
        for i in xrange(start, 10):
            path.append(i)
            self.dfs(i+1, path, res)
            path.pop()
            
#another way of backtracking
"""
        path = []
        for i in xrange(1, 10):
            path.append(i)
            self.dfs(i, path)
            path.pop()
        return self.res
            
    def dfs(self, i, path):
        if len(path)==self.k:
            if sum(path) == self.n:
                self.res.append(path[:])
            return
        for j in xrange(i+1, 10):
            path.append(j)
            self.dfs(j, path)
            path.pop()
"""
        
        


            
