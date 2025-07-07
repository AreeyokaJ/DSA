class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0 

        characters = set() 
        l = 0 

        for r in range(len(s)):
            while s[r] in characters:
                characters.remove(s[l])
                l += 1 
            characters.add(s[r])
            longest = max(longest, (r-l) + 1)

        return longest 

