class Solution:
    def minWindow(self, s: str, t: str) -> str:
        

        countT = defaultdict(int) 

        for c in t: 
            countT[c] += 1 

        
        window = defaultdict(int) 

        l = 0 
        res = [-1, -1] 
        need = len(countT)
        have = 0 
        minRes = float("inf")

        for r in range(len(s)): 
            window[s[r]] += 1 

            if window[s[r]] == countT[s[r]]:
                have += 1 

            while have == need: 
                if (r-l + 1) < minRes:
                    minRes = r - l + 1
                    res = [l, r]
                
                window[s[l]] -= 1 
        
                if s[l] in countT and window[s[l]] < countT[s[l]]: 
                    have -= 1

                l += 1

        
        return s[res[0]:res[1] + 1]

                




