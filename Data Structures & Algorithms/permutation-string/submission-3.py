class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''my soln
        '''
        # freq1 = {}
        # for c in s1:
        #     freq1[c] = freq1.get(c, 0) + 1
        
        # l, r = 0, 0
        # freq2 = {}
        # while r < len(s2):
        #     cur = s2[r]
        #     freq2[cur] = freq2.get(cur, 0) + 1
        #     # 1. cur not in s1
        #     if cur not in s1:
        #         l = r + 1
        #         freq2 = {}
        #     else:
        #         # 2. freq2[cur] == freq1[cur]
        #         if freq2[cur] == freq1[cur] and r - l + 1 == len(s1):
        #             return True
        #         # 3. freq2[cur] > freq1[cur]
        #         elif freq2[cur] > freq1[cur]:
        #             while freq2[cur] > freq1[cur]:
        #                 freq2[s2[l]] -= 1
        #                 l += 1
        #         # 4. freq2[cur] < freq1[cur]
        #     r += 1
        # return False

        '''neet: a bit verbose but nice illustration as an alternative to my soln!
        '''
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26
                    

                



            
