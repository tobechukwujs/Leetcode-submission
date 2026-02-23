class Solution(object):
    def maxProfit(self, prices):
        maxProfit = 0
        minPrice = float("inf")
        for price in prices:
            if price < minPrice:
                minPrice = price
            else:
                maxProfit = max(maxProfit, price - minPrice)
        return maxProfit        
        