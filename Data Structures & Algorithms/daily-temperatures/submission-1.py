class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        1. Brute Force
        '''
        # res = []
        # for i in range(len(temperatures)):
        #     for j in range(i + 1, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             res.append(j - i)
        #             break
        #     if len(res) <= i:
        #         res.append(0)
        # return res
        ''' REDO????
        2. Stack (monotonic stack)
        '''
        res = [0] * len(temperatures)
        stack = [] # pair: temp, idx
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res
            





