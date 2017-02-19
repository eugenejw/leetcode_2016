# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        @link https://leetcode.com/submissions/detail/93552819/
        """
        res = []
        if not intervals:
            return res
        intervals.sort(key=lambda x:x.start)
        start = intervals[0].start
        end = intervals[0].end
        for interval in intervals:
            if end >= interval.start:
                end = max(end, interval.end)
            else:
                tmp = Interval(start, end)
                res.append(tmp)
                start = interval.start
                end = interval.end
        res.append(Interval(start, end))
        return res
            
        
