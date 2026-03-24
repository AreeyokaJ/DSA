class Solution:
    def partitionLabels(self, s: str) -> List[int]:


        freq = defaultdict(int) 

        for c in s: 
            freq[c] += 1 
        ans = [] 


        seen = set()

        count = 0 

        for c in s: 
            seen.add(c)

            freq[c] -= 1 
            count += 1 

            if freq[c] == 0:
                seen.remove(c) 

            if freq[c] == 0 and len(seen) == 0:
                ans.append(count) 
                count = 0 

        return ans
                