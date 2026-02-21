class Solution:
    def numDecodings(self, s: str) -> int:
        valid = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18",
                    "19", "20", "21", "22", "23", "24", "25", "26"}


        dp = {len(s):1} 

        def dfs(i):
            if i > len(s):
                return 0 

            if i in dp:
                return dp[i]
            
            if s[i] == "0":
                return 0 

            dp[i] = dfs(i + 1)
            res = dp[i] 


            if s[i:i+2] in valid:
                res += dfs(i + 2) 
                dp[i] = res

            return res

        return dfs(0)

            