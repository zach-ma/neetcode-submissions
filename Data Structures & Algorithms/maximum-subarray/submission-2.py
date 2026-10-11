class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        include
        shift
        '''
        # l, r = 0, 1
        # curMax = nums[0]
        # cur = nums[0]
        # while r < len(nums):
        #     if cur + nums[r] >= curMax:
        #         cur += nums[r]
        #         r += 1
        #         curMax = max(curMax, cur)
        #     else:
        #         while r < len(nums) and cur + nums[r] == curMax:

        #     if cur + nums[r] < 0: # shift
        #         l = r + 1
        #         r = 
        #     else: # include

        l, r = 0, 1
        curMax = nums[0]
        cur = nums[0]
        while r < len(nums):
            if cur < 0: # remove negative prefix
                cur = nums[r]
                l = r
            else:
                cur += nums[r]
            r += 1
            curMax = max(cur, curMax)
        return curMax







