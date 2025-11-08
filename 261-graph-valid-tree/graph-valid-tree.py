class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj = {i:[] for i in range(n)}

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        
        cycle = set()
        visit = set()
        def dfs(n, prev):
            if n in cycle:
                return False 
            
            cycle.add(n)
            for nei in adj[n]:
                if nei == prev:
                    continue 

                if not dfs(nei, n): return False 
            
            cycle.remove(n)
            visit.add(n)
            return True

        return dfs(0, -1) and len(visit) == n 
