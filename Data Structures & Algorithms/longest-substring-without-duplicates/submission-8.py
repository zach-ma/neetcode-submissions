class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        1. Brute Force
        '''
        ''' REDO???
        2. Sliding Window using hash set

        T: O(n)!!!!! because l, r never back up!!!! they both increment n times at most
        S: O(m)
        '''
        # charSet = set()
        # l = 0
        # res = 0

        # for r in range(len(s)):
        #     # NOTE!!!: If we ever see a repeated character, we shrink the window from the left until the duplicate is removed.
        #     while s[r] in charSet:
        #         charSet.remove(s[l])
        #         l += 1
        #     charSet.add(s[r])
        #     res = max(res, r - l + 1)
        # return res


        ''' REDO!!!!!
        3.1 Sliding Window (Optimal using hashmap), my soln after 2 hints
        '''
        # if not s:
        #     return 0
        # seen = {} # char -> idx
        
        # curMax = 0
        # l, r = 0, 0
        # while r < len(s):
        #     if s[r] in seen and l <= seen[s[r]] < r:
        #         l = seen[s[r]] + 1
        #     curMax = max(curMax, r - l + 1)
        #     seen[s[r]] = r
        #     r += 1
        # return curMax


        ''' REDO!!!
        3.2 Sliding Window (Optimal using hashmap)

        T: O(n)!!!!! because l, r never back up!!!! they both increment n times at most
        S: O(m)
        '''
        mp = {} # NOTE: We keep a map that stores the last index where each character appeared.
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(l, mp[s[r]] + 1) # NOTE: smart to use max()!!!!!!
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res

