class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        2.0 binary search (my soln with hint)
        '''
        l, r = 1, max(piles)
        curMin = max(piles)
        while l <= r:
            m = l + (r - l) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / m)
            print(hours)
            if hours > h:
                l = m + 1
            else:
                curMin = min(m, curMin)
                r = m - 1
        return curMin