class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ''' REDO??? Cannot solve without watching entire soln!!!!
        2. Sliding Window
        window size – count of the most frequent character ≤ k
        '''
        # count = {}
        # res = 0

        # l = 0
        # for r in range(len(s)):
        #     count[s[r]] = 1 + count.get(s[r], 0)
            
        #     while (r - l + 1) - max(count.values()) > k:
        #         count[s[l]] -= 1
        #         l += 1
            
        #     res = max(res, r - l + 1)
        
        # return res

        ''' REDO??? don't understand!!!
        3. Sliding Window (Optimal)
        window size – count of the most frequent character ≤ k
        T: O(n)
        S: O(m) or O(1)
        where n is the length of the string and m is the total number of unique chars in the string => at most unique chars so O(1)
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
            
            res = max(res, r - l + 1)
        
        return res
