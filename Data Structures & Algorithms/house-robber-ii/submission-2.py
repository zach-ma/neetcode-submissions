class Solution:
    def rob(self, nums: List[int]) -> int:
        '''my failed soln
        '''
        # ..., rob1, rob2, n, n + 1, ...

        # 0, ..., i - 2, i - 1, i, 0, 1

        # # dp1 skips nums[0]
        # dp1 = [0] * len(nums)
        # if len(nums) > 1:
        #     dp1[1] = nums[1]
        # for i in range(2, len(nums)):
        #     nums[i] = max(dp1[i - 2] + nums[i], dp1[i - 1])


        # # dp2 choose nums[0]
        # dp2 = [0] * len(nums)
        # dp2[0] = nums[0]
        # if len(nums) > 1:
        #     dp2[1] = nums[1]
        # for i in range(2, len(nums)):
        #     if i == len(nums) - 1:
        #         nums[i] = dp2[i - 1]
        #     else:
        #         nums[i] = max(dp2[i - 2] + nums[i], dp2[i - 1])
        # return max(dp1[-1], dp2[-1])

        '''neet
        '''
        def helper(nums):
            rob1, rob2 = 0, 0 # NOTE: dummy is helpful!!!!
            for n in nums:
                newRob = max(rob1 + n, rob2)
                rob1, rob2 = rob2, newRob
            return rob2
        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))

        
