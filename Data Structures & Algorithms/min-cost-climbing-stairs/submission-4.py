class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        1. Recursion
        '''
        ''' REDO????
        2. Dynamic Programming (Top-Down)

        For each step i, the minimum cost to reach the top is:
            cost[i] + minimum cost from step i+1 or i+2
        '''
        memo = [-1] * len(cost)

        def dfs(i):
            if i >= len(cost):
                return 0 # beyond last step
            if memo[i] != -1:
                return memo[i]
            memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return memo[i]

        return min(dfs(0), dfs(1))

        '''
        3.1 Dynamic Programming (Bottom-Up), my soln
        '''
        # dp = [-1] * (len(cost) + 1) # NOTE: +1 to include the top floor!!!
        # dp[0], dp[1] = 0, 0
        # for i in range(2, len(cost) + 1): # NOTE: +1 to include the top floor!!!
        #     dp[i] = min(cost[i - 1] + dp[i - 1], cost[i - 2] + dp[i - 2])
        # return dp[-1]

        '''
        3.2 Dynamic Programming (Bottom-Up)
        '''
        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1],
                        dp[i - 2] + cost[i - 2])
        return dp[n]
        '''
        4. Dynamic Programming (Space Optimized)
        '''