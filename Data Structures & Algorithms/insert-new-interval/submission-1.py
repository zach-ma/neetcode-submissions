class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        my failed soln
        lesson: should not be in-place, should not use insert()
        '''
        # start, end = newInterval
        # for i, (start_i, end_i) in enumerate(intervals):
        #     if start < start_i and end < start_i: # no overlap
        #         intervals.insert(i, [start, end])
        #         break
        #     elif (end >= start_i): # has overlap
        #         intervals.insert(i, )
        # return intervals
        '''neet
        '''
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]: # non-overlapping, front
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]: # non-overlapping, back
                res.append(intervals[i])
            else: # overlapping
                newInterval = [min(newInterval[0], intervals[i][0]),
                                max(newInterval[1], intervals[i][1])]
        res.append(newInterval) # if the first "if" condition never executes, we will never have a chance to add newInterval to res
        return res