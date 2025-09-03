class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        adjacency = {i:[] for i in range(n)}


        for n1, n2 in edges:
            adjacency[n1].append(n2)
            adjacency[n2].append(n1)

        
        visit = set()


        def dfs(node, prev):
            if node in visit:
                return False 

            visit.add(node)

            for nei in adjacency[node]:
                if prev == nei:
                    continue 
                
                if not dfs(nei, node): return False 
            

            return True 

        
        return dfs(0, -1) and len(visit) == n