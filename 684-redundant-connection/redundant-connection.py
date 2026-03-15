class UnionFind:

    def __init__(self, n):
        self.par = {}
        self.rank = {} 

        for i in range(1, n+ 1):
            self.par[i] = i
            self.rank[i] = 0 

    def find(self, n):
        p = self.par[n] 
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]] 
            p = self.par[p]
        
        return p



class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        union = UnionFind(len(edges))

        for n1, n2 in edges:
            p1, p2 = union.find(n1), union.find(n2)
            if p1 == p2:
                return [n1, n2]
            
            if union.rank[p1] > union.rank[p2]:
                union.par[p2] = p1 
            elif union.rank[p2] < union.rank[p1]:
                union.par[p1] = p2 

            else: 
                union.par[p1] = p2 
                union.rank[p2] = union.rank[p1] + 1
            


        

