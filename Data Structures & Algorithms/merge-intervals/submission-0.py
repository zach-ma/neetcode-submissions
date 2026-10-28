class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda interval: interval[0])
        res = []
        for cur in sorted_intervals:
            if not res:
                res.append(cur)
            else:
                prev = res.pop()
                if prev[1] >= cur[0]: # overlapping
                    res.append([prev[0], max(prev[1], cur[1])])
                else:
                    res.append(prev)
                    res.append(cur)
        return res


