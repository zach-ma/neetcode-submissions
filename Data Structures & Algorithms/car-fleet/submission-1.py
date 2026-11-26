class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''my impl after hint
        '''
        # pairs = [[p, s] for p, s in zip(position, speed)]
        # stack = []
        # for p, s in sorted(pairs)[::-1]: # reverse sorted order
        #     t = (target - p) / s
        #     if stack and stack[-1] >= t:
        #         continue
        #     stack.append(t)
        # return len(stack)
        '''neet
        '''
        pairs = [[p, s] for p, s in zip(position, speed)]
        
        stack = []
        for p, s in sorted(pairs)[::-1]: # reverse sorted order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
        


