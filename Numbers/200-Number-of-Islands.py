Bclass Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        :@see https://leetcode.com/problems/number-of-islands/
        """
        #grid = map(list, grid)
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        res = 0
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == '1':
                    res += 1
                    self.dfs(grid, i, j)
        return res
                
    def dfs(self, grid, i, j):
        if i == len(grid) or j == len(grid[0]) or i < 0 or j < 0:
            return
        if grid[i][j] == '0':
            return
        
        grid[i][j] = '0'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i, j-1)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
