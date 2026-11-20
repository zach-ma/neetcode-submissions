class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''soln (greg hogg)
        '''
        res = [0] * len(temperatures)

        monstack = []
        for i, temp in enumerate(temperatures):
            while monstack and monstack[-1][1] < temp:
                prev_i, prev_temp = monstack.pop()
                res[prev_i] = i - prev_i
            monstack.append((i, temp))
        return res