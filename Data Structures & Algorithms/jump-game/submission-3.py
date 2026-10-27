class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''my soln: greedy
        '''
        # cur = 0
        # for n in nums:
        #     if cur < 0:
        #         return False
        #     if n > cur:
        #         cur = n
        #     cur -= 1
        # return True

        '''
        neet: greedy in reverse order
        idea: continuously shifting goal post towards left
        '''
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i # shift goal post closer to us
        return goal <= 0









