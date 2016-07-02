"""
https://leetcode.com/problems/top-k-frequent-elements/
"""

#import heapq
import itertools
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #bucket sort
        d = dict()
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        #print "d is {}".format(d)
        bucket = [[] for _ in nums]
        for num, count in d.items():
            bucket[len(nums)-count].append(num)
        
        return list(itertools.chain(*bucket))[:k]
        
        """
        #using priority queue (logn time to build binary tree)
        pq = []
        for num, count in d.items():
            heapq.heappush(pq, (count, num))
        res = map(lambda x: x[1], [heapq.heappop(pq) for i in xrange(len(pq))])
        
        return res[len(res)-k:]
        """
