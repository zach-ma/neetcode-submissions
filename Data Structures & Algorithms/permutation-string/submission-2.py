class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = {}
        for c in s1:
            freq1[c] = freq1.get(c, 0) + 1
        
        l, r = 0, 0
        freq2 = {}
        while r < len(s2):
            cur = s2[r]
            freq2[cur] = freq2.get(cur, 0) + 1
            # 1. cur not in s1
            if cur not in s1:
                l = r + 1
                freq2 = {}
            else:
                # 2. freq2[cur] == freq1[cur]
                if freq2[cur] == freq1[cur] and r - l + 1 == len(s1):
                    return True
                # 3. freq2[cur] > freq1[cur]
                elif freq2[cur] > freq1[cur]:
                    while freq2[cur] > freq1[cur]:
                        freq2[s2[l]] -= 1
                        l += 1
                # 4. freq2[cur] < freq1[cur]
            r += 1
        return False
                    

                



            
