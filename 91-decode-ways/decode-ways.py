class Solution:
    def numDecodings(self, s: str) -> int:
        valid = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18",
                    "19", "20", "21", "22", "23", "24", "25", "26"}



        dp = {len(s):1} 


        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0 

            else:
                dp[i] = dp[i + 1]

            if i < len(s) - 1 and  s[i:i + 2] in valid:
                dp[i] += dp[i + 2] 

        return dp[0]


        # def dfs(i):
        #     if i in dp:
        #         return dp[i]
            
        #     if  i > len(s) or s[i] == "0" :
        #         return 0 

            
        #     res = dfs(i + 1) 
        #     dp[i] = res 

        #     if s[i: i + 2] in valid:
        #         res += dfs(i + 2) 
        #         dp[i] = res 
            
        #     return res 

        return dfs(0)
