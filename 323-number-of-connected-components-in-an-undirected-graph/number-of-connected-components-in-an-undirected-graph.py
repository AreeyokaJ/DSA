class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = {i:[] for i in range(n)}

        for n1, n2 in edges: 
            adj[n1].append(n2) 
            adj[n2].append(n1)

        visit = set() 

        def dfs(node):
            if node in visit:
                return 
            
            visit.add(node) 

            for nei in adj[node]:
                dfs(nei) 
        

        connect = 0 

        for i in range(n):
            if i not in visit:
                connect += 1 
                dfs(i) 

        return connect