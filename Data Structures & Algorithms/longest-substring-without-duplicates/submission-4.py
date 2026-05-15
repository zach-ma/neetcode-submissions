class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        seen = {} # char -> idx
        
        curMax = 0
        l, r = 0, 0
        while r < len(s):
            if s[r] not in seen:
                curMax = max(curMax, r - l + 1)
            else:
                if l <= seen[s[r]] < r:
                    l = seen[s[r]] + 1
            curMax = max(curMax, r - l + 1)
            seen[s[r]] = r
            r += 1
        return curMax
