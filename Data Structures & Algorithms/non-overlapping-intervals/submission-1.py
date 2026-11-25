class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''neet: greedy
        '''
        intervals.sort()

        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd: # non-overlapping
                prevEnd = end
            else:
                res += 1 # remove one of the intervals
                prevEnd = min(prevEnd, end)

        return res

