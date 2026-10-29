class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''neet
        '''
        count = {}
        l, r = 0, 0
        res = 0
        while r < len(s):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxFreq = max(count.values())
            length = r - l + 1
            if length - maxFreq <= k:
                res = max(res, length)
            else:
                while (r - l + 1) - max(count.values()) > k and l < r:
                    count[s[l]] -= 1
                    l += 1
            r += 1
        return res

