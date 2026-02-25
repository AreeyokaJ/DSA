class Solution:
    def numDecodings(self, s: str) -> int:
        
        valid = {"10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "26", "25"}

        dp = {len(s): 1}
        
        for i in range(len(s) -1, -1, -1):

            if s[i] == "0":
                dp[i] = 0 
            else:
                dp[i] = dp[i + 1] 

            if i < len(s) - 1 and s[i: i +2] in valid:
                dp[i] += dp[i+2]

        
        return dp[0]