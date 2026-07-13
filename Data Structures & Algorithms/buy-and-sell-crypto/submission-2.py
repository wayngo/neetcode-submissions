class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxBuy = 0 
        minBuy = prices[0]

        for sell in prices:
            maxBuy = max(maxBuy, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxBuy