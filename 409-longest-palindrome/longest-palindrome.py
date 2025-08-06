class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        chars = defaultdict(int)

        for char in s:
            chars[char] += 1 
            print(char, chars[char])
        
        longest = 0 
        longest_odd = 0
        oddFound = False
    
        
        for key in chars:
            if chars[key] % 2 == 0:
                longest += chars[key]

            else:
                longest += chars[key] - 1
                oddFound = True
            
        if oddFound:
            longest += 1 
            print(oddFound)
     
        
        return longest


            
