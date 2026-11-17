class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r, curK = 1, max(piles), max(piles)
        while l <= r:
            m = l + (r - l) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / m)
            if hours > h:
                l = m + 1
            else:
                r = m - 1
                curK = min(curK, m)
        return curK
