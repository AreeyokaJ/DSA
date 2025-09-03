class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adj = {i:[] for i in range(n)}


        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        
        #we start with one node 0 
            #run dfs and add the nodes to visit 
            #connected components = 1 

        #we cycle through the rest of the nodes
            #if the node is in visit thenn we continue 

            #if the node is not in vist then we run dfs again 
                #connected components = 2 

        visit = set() 

        def dfs(node):
            visit.add(node)

            for nei in adj[node]:
                if nei in visit:
                    continue 
                
                dfs(nei) 

        
        connected = 1 
        dfs(0)

        for n in range(1, n):
            if n in visit:
                continue 
            
            connected += 1

            dfs(n) 
        
        return connected