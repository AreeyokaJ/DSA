class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(s) < len(t):
            return ""


        needMap = defaultdict(int) 
        haveMap = defaultdict(int) 

        for c in t:
            needMap[c] += 1

        need = len(needMap)
        have = 0 

        l = 0
        min_size = float("inf")
        result = (0, 0)



        for r in range(len(s)):
            if s[r] in needMap:
                haveMap[s[r]] += 1 
                if haveMap[s[r]] == needMap[s[r]]:
                    have += 1 

            while have == need:
                curr_size = (r -l) + 1

                if curr_size < min_size:
                    min_size = curr_size
                    result = (l, r)

                if s[l] in needMap:
                    if haveMap[s[l]] == needMap[s[l]]:
                        have -= 1
                    
                    haveMap[s[l]] -= 1

                l += 1

        l, r = result
    
        return s[l:r + 1] if min_size < float("inf") else ""
