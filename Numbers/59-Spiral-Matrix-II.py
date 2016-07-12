class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        https://leetcode.com/problems/spiral-matrix-ii/
        """
        #Matrix Walk
        A = [[0]*n for _ in xrange(n)]
        #d indicates direction
        i, j, di, dj = 0, 0, 0, 1
        for k in xrange(1, n*n+1):
            A[i][j] = k
            if A[(i+di)%n][(j+dj)%n]:
                #swap directions
                di, dj = dj, -di
            i += di
            j += dj
            
        return A
        


class Solution(object):
    #not so graceful matrix rotation
    #https://leetcode.com/problems/spiral-matrix-ii/
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        N = [i for i in xrange(1, n*n)]
        A = [[n*n]]
        while N:
            A = self.rotate(A)
            tmp_lst = []
            for i in xrange(len(A[0])):
                tmp = N.pop()
                tmp_lst.append(tmp)
            tmp_lst.reverse()
            A.insert(0, tmp_lst)
            
        return A
            
    def rotate(self, A):
        #print "A0 is {}".format(A)
        A = map(list, zip(*A))
        #print "A1 is {}".format(A)
        for lst in A:
            lst.reverse()
        return A
            
        
