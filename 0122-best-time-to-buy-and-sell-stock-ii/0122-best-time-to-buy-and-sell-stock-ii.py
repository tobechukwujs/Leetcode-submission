class Solution(object):
    def maxProfit(self, prices):
        maxProfit = 0
        minPrice = float('inf')

        for i in range (1, len(prices)):
            if prices[i] > prices[i- 1] :
                maxProfit += prices[i] - prices[i- 1]   
        return maxProfit 