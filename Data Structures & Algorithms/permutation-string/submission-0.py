class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_original = {}
        for c in s1:
            freq_original[c] = 1 + freq_original.get(c, 0)
       
        freq = freq_original.copy()
        n = len(s1)
        l, r = 0, 0
        while r < len(s2):
            if s2[r] not in freq: # 1. not in freq
                l = r + 1
                freq = freq_original.copy()
            else:
                if freq[s2[r]] > 0: # 2. happy path
                    freq[s2[r]] -= 1
                else: # 3. freq used up
                    while freq[s2[r]] == 0:
                        freq[s2[l]] += 1
                        l += 1
                    # now freq[s2[r]] == 1
                    freq[s2[r]] -= 1
            print(freq)
            r += 1
            if r - l == n:
                return True
        return False


        




