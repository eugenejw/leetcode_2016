from heapq import heappush, heappop
from collections import namedtuple
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        @link https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
        """
        #init the heap O(k)
        Pair = namedtuple('Pair', 'x y')
        if not nums1 or not nums2:
            return []
        pq = []
        for i in xrange(min(k, len(nums1))):
            p = Pair(nums1[i], nums2[0])
            heappush(pq, (p.x+p.y, [p.x, p.y], (i, 0)))
            
        res = []
        for _ in xrange(k):
            if len(pq) == 0:
                break
            tmp = heappop(pq)
            res.append(tmp[1])
            i, j = tmp[2]

            if j+1 < len(nums2):
                p = Pair(nums1[i], nums2[j+1])
                heappush(pq, (p.x+p.y, [p.x, p.y], (i, j+1)))
        return res
        
        
