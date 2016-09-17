class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        :@see https://discuss.leetcode.com/topic/1978/a-n-2-solution-can-we-do-better/2
        """
        nums.sort()
        best = 0
        for i in xrange(3):
            best += nums[i]
        
        for i in xrange(len(nums)-2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                cur_sum = nums[i] + nums[j] + nums[k]
                if abs(target - best) > abs(target - cur_sum):
                    best = cur_sum
                    
                if cur_sum > target:
                    k -= 1
                elif cur_sum < target:
                    j += 1
                else:
                    return target
                    
        return best
        
