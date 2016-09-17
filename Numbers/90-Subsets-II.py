class Solution(object):
    '''
    @link https://leetcode.com/problems/subsets-ii/
    @using backtrace 
    '''
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        self.dfs(0, nums, res, [])
        return res+[[]]
        
    def dfs(self, begin, nums, res, path):
        for i in xrange(begin, len(nums)):
            #print 'i -> {}'.format(i)
            if i == begin or nums[i] != nums[i-1]:
                path.append(nums[i])
                #print 'path -> {}'.format(path)
                res.append(path[:])
                self.dfs(i+1, nums, res, path)
                path.pop()
        
