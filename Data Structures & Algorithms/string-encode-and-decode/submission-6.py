class Solution:

    def encode(self, strs: List[str]) -> str:
        '''
        ['abc', 'de'] -> '3#abc2#de'
        '''
        encoded = ''
        for s in strs:
            encoded += str(len(s)) + '#' + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            # get length
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            # get string
            decoded.append(s[j + 1: j + 1 + length])
            i = j + 1 + length # CRITICAL: update i precisely!!!
        return decoded