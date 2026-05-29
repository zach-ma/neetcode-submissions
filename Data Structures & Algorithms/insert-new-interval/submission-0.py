class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        my failed soln
        '''
        # for i, inter in enumerate(intervals):
        #     if newInterval[1] < inter[0]: # 1. new is left side of old
        #         intervals.insert(i, newInterval)
        #     elif newInterval[0] <=
        #     elif inter[0] <= newInterval[1]: # 2. new overlaps partial left of old
        #         intervals[i][0] = newInterval[0]
        #     elif inter[0] <= newInterval[0] and newInterval[1] <= inter[1]: # 3. new contained entirely by old
        ''' REDO!!!
        1. Linear Search
        '''
        ''' REDO!!!
        2. Binary Search
        '''
        ''' REDO!!!
        3. Greedy
        '''
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]: # 1. non-overlapping, to the left
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]: # 2. non-overlapping, to the right
                res.append(intervals[i])
            else: # 3. overlap => merge
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        res.append(newInterval) # CRITICAL!!!!!!! here we never inserted newInterval so we insert before return
        return res

