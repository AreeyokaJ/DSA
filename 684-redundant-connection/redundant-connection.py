class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    

        adj = {i:[] for i in range(1, len(edges) + 1)}


        
        visit = set() 
        cycle = set()
        ans = []
        def dfs(i, prev):
            if i in visit: 
                return True 
            
            if i in cycle:
                return False

            cycle.add(i) 

            for nei in adj[i]:
                if nei == prev:
                    continue 

                if not dfs(nei, i): 
                    ans.append([i, nei])
                    return False 

            cycle.remove(i)
            visit.add(i)
            return True 

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1) 

            for i in range(1, len(edges) + 1):
                if not dfs(i, -1):
                    return [n1, n2]

            
            visit = set()
            cycle = set()


