class Solution:
    def rob(self, nums: List[int]) -> int:
        '''my failed soln
        lesson: thought it was greedy, but actually dp
        '''
        # cur = nums[0]
        # adjacent = True
        # for i in range(1, len(nums)):
        #     new = cur - nums[i - 1] + nums[i]
        #     if adjacent:
        #         if new > cur:
        #             cur = new
        #         else: # skip i
        #             adjacent = False
        #     else:
        #         cur += nums[i]
        #         adjacent = True
        # return cur
        '''my failed soln after hint
        '''
        # if not nums:
        #     return 0
        # return max(nums[0] + self.rob(nums[2:]), self.rob(nums[1:]))
        '''neet: dp using two pointers
        '''
        rob1, rob2 = 0, 0
        for n in nums:
            # ..., rob1, rob2, n, n + 1, ...
            temp = max(n + rob1, rob2)
            rob1, rob2 = rob2, temp
        return rob2
            
