class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        1. Recursion
        '''
        ''' REDO????
        2. Dynamic Programming (Top-Down)
        '''
        '''
        3.1 Dynamic Programming (Bottom-Up), my soln
        '''
        dp = [-1] * (len(cost) + 1) # NOTE: +1 to include the top floor!!!
        dp[0], dp[1] = 0, 0
        for i in range(2, len(cost) + 1): # NOTE: +1 to include the top floor!!!
            dp[i] = min(cost[i - 1] + dp[i - 1], cost[i - 2] + dp[i - 2])
        return dp[-1]
        
        '''
        3.2 Dynamic Programming (Bottom-Up)
        '''
        '''
        4. Dynamic Programming (Space Optimized)
        '''