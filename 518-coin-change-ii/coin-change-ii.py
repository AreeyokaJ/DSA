class Solution:
    def change(self, amount: int, coins: List[int]) -> int:



        cache = {}
    
        def dfs(i, total, count):

            if total == amount:
                return 1 

            if total > amount or  i >= len(coins): 
                return 0

            if (i, total) in cache: 
                return cache[(i, total)]

            

            count1 = dfs(i, total + coins[i], count)
            count2 = dfs(i + 1, total , count) 



            cache[(i, total)] = count1 + count2 

            return cache[(i,total)] 

        return dfs(0, 0, 0)
