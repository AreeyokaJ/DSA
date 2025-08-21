class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longest = 0 
        chars = set()

        l = 0 

        for r in range(len(s)):
            
            while s[r] in chars: 
                chars.remove(s[l])
                l += 1 
            
            chars.add(s[r])
            longest = max(r - l + 1, longest)

        return longest