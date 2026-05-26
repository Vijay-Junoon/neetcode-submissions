class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        b = prices[0]
        for  i in range(1,len(prices)):
            if prices[i] < b:
                b  = prices[i]
            profit = max(profit,prices[i] - b)
        return profit