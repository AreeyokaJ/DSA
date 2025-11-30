class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0 
        max_length = 0 

        freq = {}

        max_repeating = 0 

        for r in range(len(s)):

            freq[s[r]] = freq.get(s[r], 0) + 1 
            max_repeating = max(max_repeating, freq[s[r]])

            while (r - l + 1) - max_repeating > k:
                freq[s[l]] -= 1 
                l += 1 
            
            max_length = max(max_length, r- l + 1) 

        return max_length


