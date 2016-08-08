class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        https://leetcode.com/problems/minimum-path-sum/
        """
        #iterative solution
        n = len(grid[0]) #length
        m = len(grid) #height
        for i in xrange(1, n):
            grid[0][i] += grid[0][i-1]
        for j in xrange(1, m):
            grid[j][0] += grid[j-1][0]

        for i in xrange(1, m):
            for j in xrange(1, n):
                grid[i][j] = min(grid[i-1][j], grid[i][j-1])+grid[i][j]
                
        return grid[m-1][n-1]
        
        
"""
#recursive solution
import copy
class Solution(object):
    def __init__(self):
        self.memo = None
        
    def minPathSum(self, grid):

        self.memo = copy.deepcopy(grid)
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                #print "i, j: {} {}".format(i, j)
                self.memo[i][j] = None
        #init the 1st row
        self.memo[0][0] = grid[0][0]
        for j in xrange(1, len(grid[0])):
            self.memo[0][j] = self.memo[0][j-1] + grid[0][j]
        for i in xrange(1, len(grid)):
            self.memo[i][0] = self.memo[i-1][0] + grid[i][0]

        i = len(grid)-1
        j = len(grid[0])-1
        return self.opt(i, j, grid)
        
    def opt(self, i, j, grid):
        if i==0 or j==0:
            return self.memo[i][j]
            
        if not self.memo[i][j]:
            self.memo[i][j] = min(self.opt(i-1, j, grid), self.opt(i, j-1, grid))+grid[i][j]
            
        return self.memo[i][j]
        
        
        
"""
