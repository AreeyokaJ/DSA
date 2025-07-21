class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        #create a frequency map of t
        freqT = {}
        for char in t:
            freqT[char] = freqT.get(char, 0) + 1

        #counter alg  ^^^^^^

        l,r = 0,0 
        
        min_length = len(s)
        res = "" 
        
        while r < len(s): 
        
            if s[r] in freqT:
                freqT[s[r]] -= 1 
            #while(current window not valid adjust r until window is valid)
            while (not self.isValidWindow(freqT)) and r < len(s):
                r += 1

                if r < len(s) and s[r] in freqT:
                    freqT[s[r]] -= 1 
            
            curr_length = (r - l) + 1 
        
            #if current_window_length < minlength: 
            if curr_length < min_length:
                
                #update min_length to be min(current window, min_length)
                min_length = curr_length 
            
                #update result substring to be substring of s (l, r)
                res = s[l:r+1]


            #while current_window is valid 
            while(self.isValidWindow(freqT)) and l < len(s):
                curr_length = (r - l) + 1 
                
                #if current_window_length < minlength: 
                if curr_length <= min_length:
                    #update min_length 
                    min_length = curr_length 

                    #update result substring 
                    res = s[l:r+1]

                if s[l] in freqT:
                    freqT[s[l]] += 1 

                l += 1

            r += 1 

        return res
        
    def isValidWindow(self, f_map):
        for key in f_map:
            if f_map[key] > 0:
                return False 
        return True 
