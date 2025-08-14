class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        
        diff = {}
        same = {}
        odds = 0 
        res = 0

        for word in words: 
            if word[0] == word[1]:
                same[word] = same.get(word, 0) + 1
                res += 2 
            
            else: 
                rev = word[1] + word[0] 
                if rev in diff and diff[rev] > 0:
                    diff[rev] -= 1 
                    res += 4 
                else:
                    diff[word] = diff.get(word, 0) + 1 
            

        for word in same: 
            if same[word] % 2 == 1:
                odds += 1

                if odds > 1:
                    res -= 2 
            
        return res


        