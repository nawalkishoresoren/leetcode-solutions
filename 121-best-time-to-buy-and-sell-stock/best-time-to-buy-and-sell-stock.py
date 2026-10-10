class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minSoFar = prices[0]
        maxProfit = 0
        for price in prices:
            minSoFar = min(minSoFar, price)
            currProfit = price - minSoFar
            print(f"CurProfit = {currProfit}")

            maxProfit = max(maxProfit,currProfit)
        
        return maxProfit
        