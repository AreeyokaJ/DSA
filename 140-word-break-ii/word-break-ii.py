class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        

        def backtrack(i):
            if i == len(s):
                ans.append(" ".join(res))
                return 
            
            for j in range(i, len(s)):
                word = s[i:j + 1]
                if word in wordDict:
                    
                    res.append(word)
                    backtrack(j + 1)
                    res.pop()
                
        wordDict = set(wordDict)
        ans = [] 
        res = [] 
        backtrack(0)

        return ans
