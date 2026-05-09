class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        1. brute force
        T: O(n^2)
        S: O(1)
        '''
        # res = 0
        # for i in range(len(prices)):
        #     buy = prices[i]
        #     for j in range(i+1, len(prices)):
        #         sell = prices[j]
        #         res = max(res, sell - buy)
        # return res

        '''
        2. Two Pointers

        Intuition

        We want to buy at a low price and sell at a higher price that comes after it.
        Using two pointers helps us track this efficiently:

            l is the buy day (looking for the lowest price)
            r is the sell day (looking for a higher price)

        If the price at r is higher than at l, we can make a profit — so we update the maximum.
        If the price at r is lower, then r becomes the new l because a cheaper buying price is always better.

        By moving the pointers this way, we scan the list once and always keep the best buying opportunity.

        '''
        l, r = 0, 1
        maxP = 0
        while r < len(prices):
            buy = prices[l]
            sell = prices[r]
            if buy < sell:
                maxP = max(maxP, sell - buy)
            else:
                l = r
            r += 1
        return maxP





























