class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        if len(s1) > len(s2):
            return False

        s1_count = defaultdict(int) 
        
        for c in s1: 
            s1_count[c] += 1 

        have = 0 
        need = len(s1_count) 
        count = defaultdict(int) 

        for i in range(len(s1)): 
            c = s2[i]
            count[c] += 1 
            if count[c] == s1_count[c]:
                have += 1 

        if have == need:
            return True 
    
        for i in range(len(s1), len(s2)): 
            c_prev = s2[i - len(s1)] 
            c_curr = s2[i]

            #update hashmap 
            
            if count[c_prev] == s1_count[c_prev]:
                have -= 1 
            
            count[c_prev] -= 1 
            
            count[c_curr] += 1 
            if count[c_curr] == s1_count[c_curr]:
                have += 1 

            if have == need:
                return True 

        print(s1_count) 
        print(count)
        return False
