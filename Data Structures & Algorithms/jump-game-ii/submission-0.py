class Solution:
    def jump(self, nums: List[int]) -> int:
        # cur = 0
        # count = 0
        # i = 0
        # while i < len(nums):
        #     j = max
        #     for j in range(i + 1, i + nums[i] + 1):


        # for i in range(len(nums)):
        #     if cur + nums[i] >= len(nums) - 1:
        #         return count
        '''neet
        '''
        res = 0
        l = r = 0
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(i + nums[i], farthest)
            res += 1
            if farthest >= len(nums) - 1:
                return res
            l, r = r + 1, farthest
        return res

