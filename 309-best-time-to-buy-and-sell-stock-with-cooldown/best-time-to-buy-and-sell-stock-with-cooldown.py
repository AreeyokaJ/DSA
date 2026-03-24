class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       
        cache = {} 



        def dfs(i, have):

            if i >= len(prices):
                return 0 

            if (i, have) in cache:
                return cache[(i, have)]
            
            buy = 0 
            sell = 0 
            nothing = 0 

            if not have:
                buy = dfs(i + 1, True) - prices[i]

            if have:
                sell = dfs(i + 2, False)  + prices[i]


            nothing = dfs(i + 1, have) 

            cache[(i, have)] = max(buy, sell, nothing)

            return cache[(i, have)]
        
        return dfs(0, False)