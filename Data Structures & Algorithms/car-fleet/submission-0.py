class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p, s] for p, s in zip(position, speed)]
        
        stack = []
        for p, s in sorted(pairs)[::-1]: # reverse sorted order
            t = (target - p) / s
            if stack and stack[-1] >= t:
                continue
            stack.append(t)
        return len(stack)
        


