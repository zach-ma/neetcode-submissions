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

        '''
        2. Dynamic Programming (Top-Down)
        '''
        memo = [-1] * len(nums)
        def dfs(i):
            if i >= len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
            return memo[i]
        return dfs(0)


        '''
        3. Dynamic Programming (Bottom-Up)
        '''
        '''
        4. Dynamic Programming (Space Optimized)
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