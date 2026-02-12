class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adj = {i: [] for i in range(n)}

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        cycle = set()
        def dfs(root, prev):
            if root in cycle:
                return False

            
            cycle.add(root)
            
            for nei in adj[root]:
                if nei == prev:
                    continue 

                if not dfs(nei, root):
                    return False 
                
            return True 

    
        return dfs(0, -1) and len(cycle) == n

        
