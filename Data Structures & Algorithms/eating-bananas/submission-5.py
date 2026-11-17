class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''my soln (after trial and error)
        '''
        # l, r, curK = 1, max(piles), max(piles)
        # while l <= r: # NOTE: <= to include the == case!!!!
        #     m = l + (r - l) // 2
        #     hours = 0
        #     for p in piles:
        #         hours += math.ceil(p / m) # math.ceil()!!!!!!!
        #     if hours > h:
        #         l = m + 1
        #     else:
        #         r = m - 1
        #         curK = min(curK, m)
        # return curK

        '''neet
        '''
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = l + (r - l) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            if hours <= h:
                r = k - 1
                res = min(res, k)
            else:
                l = k + 1
        return res



