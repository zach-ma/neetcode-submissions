class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        1. Recursion
        '''
        # if n <= 2:
        #     return n
        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)


        ''' REDO???
        2. Dynamic Programming (Top-Down)
        '''
        # cache = [-1] * n
        # def dfs(i):
        #     if i >= n:
        #         # NOTE!!!: If i == n: you've reached the destination exactly → count this as 1 valid way.
        #         # If i > n: you went past the destination → count this as 0 valid ways.
        #         return i == n
        #     if cache[i] != -1:
        #         return cache[i]
        #     cache[i] = dfs(i + 1) + dfs(i + 2)
        #     return cache[i]
        # return dfs(0)

        '''
        3. Dynamic Programming (Bottom-Up)
        '''
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2 # 1, 2 are base case
        for i in range(3, n + 1): # start from 3
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


        '''
        4. Dynamic Programming (Space Optimized)
        '''
        # if n <= 2:
        #     return n
        # arr = [0] * (n + 1)
        # arr[1] = 1
        # arr[2] = 2
        # for i in range(3, n + 1):
        #     arr[i] = arr[i - 2] + arr[i - 1]
        # return arr[-1]
