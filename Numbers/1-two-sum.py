lass Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        buffDict = dict()
        for i in xrange(len(nums)):
            #print target-nums[i]
            if nums[i] in buffDict:
                return [buffDict[nums[i]], i]
            else:
                #print '{} not in dic'.format(target-nums[i])
                buffDict[target-nums[i]] = i
            #print buffDict
