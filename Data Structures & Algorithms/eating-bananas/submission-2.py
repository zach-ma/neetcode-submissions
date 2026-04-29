class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        1. brute force
        T: O(m * n), where n is the length of the input array piles and m is the maximum number of bananas in a pile.
        S: O(1)
        '''
        # speed = 1
        # while True:
        #     totalTime = 0
        #     for pile in piles:
        #         totalTime += math.ceil(pile / speed)
        #     if totalTime <= h:
        #         return speed
        #     speed += 1
        # return speed

        ''' REDO!!!
        2.0 binary search (my soln with hint)
        LESSON: identify where to apply binary search
        '''
        # l, r = 1, max(piles)
        # curMin = max(piles)
        # while l <= r:
        #     m = l + (r - l) // 2
        #     hours = 0
        #     for pile in piles:
        #         hours += math.ceil(pile / m)
        #     print(hours)
        #     if hours > h:
        #         l = m + 1
        #     else:
        #         curMin = min(m, curMin)
        #         r = m - 1
        # return curMin

        ''' REDO!!!
        2.1 Binary Search
        T: O(n * logm), where n is the length of the input array piles and m is the maximum number of bananas in a pile.
        S: O(1)
        '''
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = l + (r - l) // 2
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile / k)
            if totalTime <= h:
                res = k # NOTE: clever way to get rid of using curMin to keep track, since it's updated only smaller number occurs
                r = k - 1
            else:
                l = k + 1
        return res





