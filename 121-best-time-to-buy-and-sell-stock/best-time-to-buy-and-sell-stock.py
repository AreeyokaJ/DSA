class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0 
        r = 1 

        max_profit = 0 

        if len(prices) == 1:
            return 0 

        while r < len(prices):
            
            profit = prices[r] - prices[l]

            if profit > max_profit:
                max_profit = profit 

            elif profit < 0:
                l = r 
            
            r += 1 

        return max_profit
            