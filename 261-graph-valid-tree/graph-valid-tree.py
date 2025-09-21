class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
    
        #tree is connected 
        #no cycles 

        adj = {i:[] for i in range(n)}

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1) 


        visit = set() 

        def dfs(node, prev):
            if node in visit:
                return False

            visit.add(node)
            for nei in adj[node]:
                if nei == prev:
                    continue 
                
                if not dfs(nei, node): return False

            return True 

        
        return True if dfs(0, -1) and len(visit) == n else False
            

