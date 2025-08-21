class Solution:
    def longestPalindrome(self, words: List[str]) -> int:


        length = 0 
        odd = False 

        same = defaultdict(int)
        different = defaultdict(int)

        for word in words: 
            if word[0] != word[1]: 
                reverse = word[1] + word[0]
                if reverse in different and different[reverse] > 0: 
                    different[reverse] -= 1 
                    length += 4  
                else: 
                    different[word] += 1

            else: 
                same[word] += 1  

            
        
        for word in same: 
            length += same[word] // 2 * 4
            if same[word] % 2 == 1: 
                odd = True 

        return length + 2 if odd else length 

        
