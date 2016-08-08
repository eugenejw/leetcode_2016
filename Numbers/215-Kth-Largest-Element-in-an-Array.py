from heapq import (
    heappop, heappush
    )
import random
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        https://leetcode.com/problems/kth-largest-element-in-an-array/
        """
        #quick selection algorithm O(n)
        #randomizing
        for i in xrange(len(nums)):
            ran = random.randint(0, len(nums)-1)
            nums[i], nums[ran] = nums[ran], nums[i]
            
        start, stop = 0, len(nums)-1
        target, pi = len(nums)-k, len(nums)-1
        pi = self.findPivot(start, stop, nums)
        while target != pi:
            if pi > target:
                stop = pi - 1
                pi = self.findPivot(start, stop, nums)
            else:
                start = pi + 1
                pi = self.findPivot(start, stop, nums)
        return nums[target]
        
    def findPivot(self, start, stop, nums):
        """find the pivot,
        #@ return type int
        """
        if start == stop:
            return start
        pi = start
        pivot = stop
        for i in xrange(start, stop):
            #print nums[i]
            if nums[i] <= nums[pivot]:
                nums[i], nums[pi] = nums[pi], nums[i]
                pi += 1
        nums[pivot], nums[pi] = nums[pi], nums[pivot]
        #print "pi is {}".format(pi)
        return pi
        
        
        
        
        
        
        #solution2 O(nlogk)
        #h = []
        #for num in nums:
        #    heappush(h, num)
        #    if len(h) > k:
        #        heappop(h)
        #return heappop(h)
        
        #solution1 O(nlogn)
        #nums.sort()
        #return nums[len(nums)-k]
