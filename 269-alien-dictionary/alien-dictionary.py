class Solution:
    def alienOrder(self, words: List[str]) -> str:

        
        adj = {c:set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            min_len = min(len(w1), len(w2)) 

            if (w1[:min_len] == w2[:min_len]) and len(w1) > len(w2):
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j]) 
                    break

        visited = set()
        cycle = set()
        ans = []

        def dfs(c):
            if c in cycle: 
                return False 

            if c in visited:
                return True 

            cycle.add(c) 

            for nei in adj[c]:
                if not dfs(nei): return False 

            cycle.remove(c) 
            visited.add(c) 
        
            ans.append(c)
            return True


        
        for c in adj:
            if  not dfs(c):
                return "" 


        return "".join(reversed(ans))

        
            