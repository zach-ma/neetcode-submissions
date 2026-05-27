class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        1.1 Recursion
        '''
        # if len(nums) == 0:
        #     return 0
        # return max(nums[0] + self.rob(nums[2:]), self.rob(nums[1:]))

        
        '''
        1.2 Recursion
        '''
        # def dfs(i):
        #     if i >= len(nums):
        #         return 0
        #     return max(nums[i] + dfs(i + 2), dfs(i + 1))
        # return dfs(0)

        ''' REDO???
        2. Dynamic Programming (Top-Down)
        '''
        # memo = [-1] * len(nums)
        # def dfs(i):
        #     if i >= len(nums):
        #         return 0
        #     if memo[i] != -1:
        #         return memo[i]
        #     memo[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
        #     return memo[i]
        # return dfs(0)

        '''
        3.1 Dynamic Programming (Bottom-Up), my soln!
        '''
        # n = len(nums)
        # dp = [0] * n
        # res = 0
        # for i in range(n - 1, -1, -1):
        #     if i == n - 1:
        #         dp[i] = nums[i]
        #     elif i == n - 2:
        #         dp[i] = max(nums[i], nums[i + 1])
        #     elif i == n - 3:
        #         dp[i] = max(nums[i] + nums[i + 2], nums[i + 1])
        #     else:
        #         dp[i] = nums[i] + max(dp[i + 2], dp[i + 3])
        #     res = max(res, dp[i]) #NOTE: critical to take max() all the way!!!!
        # return res
    
        ''' REDO???
        3.2 Dynamic Programming (Bottom-Up)
        
        For each house i, the maximum money we can have depends on:

            Not robbing it → same money as i - 1
            Robbing it → money at i + best up to i - 2

        We choose the better of the two at every step.
        '''
        # if not nums:
        #     return 0
        # if len(nums) == 1:
        #     return nums[0]
        # dp = [0] * len(nums)
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])
        # for i in range(2, len(nums)):
        #     dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        # return dp[-1]


        ''' REDO??? TRY UNDERSTAND!!!
        4. Dynamic Programming (Space Optimized)
        '''
        rob1, rob2 = 0, 0
        for n in nums:
            # [..., rob1, rob2, n, n+1, ...]
            temp = max(rob1 + n, rob2)
            rob1, rob2 = rob2, temp
        return rob2 # NOTE: smart!!! no need to keep track of another variable res



        
        