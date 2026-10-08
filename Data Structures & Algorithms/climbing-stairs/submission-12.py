class Solution:
    def climbStairs(self, n: int) -> int:
        '''my failed soln
        '''
        # if n < 0:
        #     return 0
        # if n == 0:
        #     return 1
        # if n <= 2:
        #     return n
        # return max(2 + self.climbStairs(n-2), 1 + self.climbStairs(n-1))

        '''
        '''
        one, two = 1, 0
        for _ in range(n):
            one, two = one + two, one
        return one