class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''my failed soln (after 40min)
        '''
        # n = len(cost)
        # dp = [-1] * n
        # for i in range(n - 1, -1, -1):
        #     if i == n - 1:
        #         dp[i] = cost[i]
        #     elif i == n - 2:
        #         dp[i] = min(cost[i], dp[i + 1])
        #     else:
        #         dp[i] = cost[i] + min(dp[i + 2], dp[i + 1])
        # return min(dp[0], dp[1])

        '''
        '''
        n = len(cost)
        if n <= 2:
            return min(cost)
        dp = [0] * (n + 1)
        dp[2] = min(cost[0], cost[1])
        for i in range(3, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[n]
