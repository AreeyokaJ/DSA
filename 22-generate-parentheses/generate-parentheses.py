class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
  
        ans = [] 

        stack = [] 

        def dfs(i, open, close):
            if open == n and close == n: 
                ans.append("".join(stack.copy()))
                return
            
            if open < n: 
                stack.append("(")
                dfs(i + 1, open + 1, close) 
                stack.pop()

            if close < open:
                stack.append(")")
                dfs(i + 1, open, close + 1) 
                stack.pop()

        dfs(0, 0, 0)
        return ans

