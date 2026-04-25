class Solution:

    def encode(self, strs: List[str]) -> str:
        '''
        my soln (after hint)
        '''
        # res = ""
        # for s in strs:
        #     res += str(len(s)) + "#" + s
        # return res

        '''
        1. Encoding & Decoding (non-optimal): record the length of each string first, followed by a special separator, and then append all the strings together.
        '''
        # if not strs:
        #     return ""

        # # record the length of each string first
        # res = ""
        # for s in strs:
        #     res += str(len(s)) + ","

        # # followed by a special separator
        # res += "#"

        # # and then append all the strings together.
        # for s in strs:
        #     res += s
        # return res

        '''
        Encoding & Decoding (optimal)
        '''
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res


    def decode(self, s: str) -> List[str]:
        '''
        my soln (after hint)
        '''
        # res = []
        # i = 0
        # while i < len(s):
        #     size = ""
        #     while s[i] != "#":
        #         size += s[i]
        #         i += 1
        #     i += 1 # skip "#"
        #     size = int(size)
        #     res.append(s[i: i + size])
        #     i += size
        # return res

        '''
        1. Encoding & Decoding (non-optimal): record the length of each string first, followed by a special separator, and then append all the strings together.
        '''
        # if not s:
        #     return []
        
        # sizes, res, i = [], [], 0
        # while s[i] != '#':
        #     cur = ""
        #     while s[i] != ',':
        #         cur += s[i]
        #         i += 1
        #     sizes.append(int(cur))
        #     i += 1
        # i += 1

        # for sz in sizes:
        #     res.append(s[i: i + sz])
        #     i += sz
        # return res

        '''
        Encoding & Decoding (optimal): for every string, we write length#string.
        '''
        res = []
        i = 0
        while i < len(s):
            j = i # NOTE: use j as right bound!!!!
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            
            # NOTE: use i, j as left and right bound!!!!
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            
        return res










                    
            
             

