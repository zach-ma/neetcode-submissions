class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''neet
        '''
        res = 0 # fact: n ^ 0 = n
        for n in nums:
            res = res ^ n
        return res