class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        https://leetcode.com/problems/search-a-2d-matrix/
        """
        # n * m matrix convert to an array => matrix[x][y] => a[x * m + y]
        # an array convert to n * m matrix => a[x] =>matrix[x / m][x % m];
        rows = len(matrix)
        cols = len(matrix[0])
        l, r = 0, rows*cols-1
        while l<=r:
            mid = (l+r)/2
            if matrix[mid/cols][mid%cols] == target:
                return True
            if matrix[mid/cols][mid%cols] < target:
                l = mid + 1
            else:#
                r = mid - 1
                
        return False
                
        
        """Not so clear way
        col = zip(*matrix)[-1]
        l, r = 0, len(col)-1
        #print l, r
        while l <= r:
            m = (l+r) / 2
            if col[m] < target:
                l = m + 1
            elif col[m] > target:
                r = m - 1
            else:
                return True
        #print l
        if col[l] < target:
            l += 1
        if l < len(col) and target in matrix[l]:
            return True
        else:
            return False
        """
                
