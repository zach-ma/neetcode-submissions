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

        ''' REDO!!!!! can't solve without hint
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
        # l, r = 0, 1 # left=buy, right=sell
        # maxP = 0
        # while r < len(prices):
        #     buy, sell = prices[l], prices[r]
        #     if buy < sell:
        #         profit = sell - buy
        #         maxP = max(maxP, profit)
        #     else:
        #         l = r # NOTE: critical!!!!!
        #     r += 1
        # return maxP

        ''' REDO!!!! can't solve without hint
        3. DP
        recurrence relation: DP[i] = max (DP[i - 1], prices[i] - min_price_so_far)
        '''
        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)
        
        return maxP





























