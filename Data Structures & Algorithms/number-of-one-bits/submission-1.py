class Solution:
    def hammingWeight(self, n: int) -> int:
        '''my soln
        '''
        # return bin(n)[2:].count('1')
        '''neet: bit shifting
        '''
        res = 0
        while n:
            res += n % 2
            n = n >> 1
        return res
