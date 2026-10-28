class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''my soln
        '''
        # sorted_intervals = sorted(intervals, key=lambda interval: interval[0])
        # res = []
        # for cur in sorted_intervals:
        #     if not res:
        #         res.append(cur)
        #     else:
        #         prev = res.pop()
        #         if prev[1] >= cur[0]: # overlapping
        #             res.append([prev[0], max(prev[1], cur[1])])
        #         else:
        #             res.append(prev)
        #             res.append(cur)
        # return res
        '''neet
        '''
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            if lastEnd >= start:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output


