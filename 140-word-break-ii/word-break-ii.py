class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        wordDict = set(wordDict) 
        res = [] 
        combination = [] 
        def backtrack(i):
            if i == len(s):
                res.append(" ".join(combination))
                return 

            word = ""
            for i in range(i, len(s)):
                word += s[i] 
                if word in wordDict:
                    combination.append(word)
                    backtrack(i + 1) 
                    combination.pop()
            return 
        backtrack(0)
        return res
