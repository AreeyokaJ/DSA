class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
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
                if prev == nei:
                    continue

                if not dfs(nei, node): 
                    return False
            
            return True
        

        if not dfs(0, -1):
            return False
        
        if len(visit) == n:
            return True
        else:
            return False

