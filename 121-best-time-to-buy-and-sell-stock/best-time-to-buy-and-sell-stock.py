class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0 
        r = 0 
        
        max_price = 0 

        while r < len(prices):
            
            if prices[l] < prices[r]:
                max_price = max(prices[r] - prices[l], max_price)
            
            if prices[l] > prices[r]:
                l = r 
            
            r += 1 

        return max_price
