class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        
        i = 0
        while i < len(s):
            size = ""
            while s[i] != "#":
                size += s[i]
                i += 1
            i += 1 # skip "#"
            size = int(size)
            res.append(s[i: i + size])
            i += size
        return res

                    
            
             

