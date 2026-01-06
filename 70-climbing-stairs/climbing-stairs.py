class Solution:
    def climbStairs(self, n: int) -> int:


        if n == 1: 
            return 1 

        if n == 2: 
            return 2 


        i = 3 

        dp = [1, 2] 

        for i in range(i, n + 1):
            temp = dp[1]
            dp[1] = dp[0] + dp[1]

            dp[0] = temp 


        
        return dp[1]