"""
https://leetcode.com/problems/different-ways-to-add-parentheses/
Converted solution from https://discuss.leetcode.com/topic/19901/a-recursive-java-solution-284-ms
"""

class Solution(object):
    def __init__(self):
        self.ops = {'*', '+', '-'}
        
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        ret = []
        for i in xrange(len(input)):
            if input[i] in self.ops:
                part1 = input[:i]
                part2 = input[i+1:]
                ret1 = self.diffWaysToCompute(part1)
                ret2 = self.diffWaysToCompute(part2)
                for r1 in ret1:
                    for r2 in ret2:
                        if input[i] == "*":
                            ret.append(r1*r2)
                        if input[i] == "+":
                            ret.append(r1+r2)
                        if input[i] == "-":
                            ret.append(r1-r2)
                        
        if not ret:
            ret.append(int(input))
        return ret
                
