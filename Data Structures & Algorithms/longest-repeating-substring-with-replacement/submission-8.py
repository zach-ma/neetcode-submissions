class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''my impl after hint
        '''
        # count = {}
        # l, r = 0, 0
        # res = 0
        # while r < len(s):
        #     count[s[r]] = 1 + count.get(s[r], 0)
        #     maxFreq = max(count.values())
        #     length = r - l + 1
        #     if length - maxFreq <= k:
        #         res = max(res, length)
        #     else:
        #         # while length - maxFreq > k and l < r: # CRITICAL: length and maxFreq are dynamically changing after each iteration, so need to recompute everytime!!!!!!!
        #         while (r - l + 1) - max(count.values()) > k and l < r:
        #             count[s[l]] -= 1
        #             l += 1
        #     r += 1
        # return res
        
        '''neet: sliding window
        T: O(26*n) = O(n)
        '''
        count = {}
        res = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

        '''neet: sliding window (optimal, unnecessary)
        T: O(n)
        '''
        count = {}
        res = 0
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(r - l + 1, res)
        return res













