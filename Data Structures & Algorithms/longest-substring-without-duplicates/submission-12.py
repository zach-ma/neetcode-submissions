class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''my soln: hash map
        '''
        # l, r = 0, 0
        # res = 0
        # hm = {} # char -> index
        # while r < len(s):
        #     c = s[r]
        #     if c in hm and hm[c] >= l: # found duplicate, shrink left window
        #         l = hm[c] + 1
        #     # expand right window
        #     hm[c] = r
        #     res = max(res, r - l + 1)
        #     r += 1
        # return res

        '''neetcode: hash set
        '''
        l = 0
        res = 0
        charSet = set()
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res

        
        



