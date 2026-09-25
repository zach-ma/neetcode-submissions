class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # res = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         profit = prices[j] - prices[i]
        #         res = max(res, profit)
        # return res

        cur_max = 0
        l, r = 0, 0
        while l <= r and r < len(prices):
            profit = prices[r] - prices[l]
            if profit < 0: # found new low
                l = r
            else:
                cur_max = max(cur_max, profit)
            r += 1
        return cur_max





