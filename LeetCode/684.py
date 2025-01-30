class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1]*n
    
    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, v0, v1):
        vid0,vid1 = self.find(v0),self.find(v1)
        if vid0 == vid1: return False
        if self.size[vid0]<self.size[vid1]:
            self.size[vid1] += self.size[vid0]
            self.parent[vid0] = self.parent[vid1]
        else:
            self.size[vid0] += self.size[vid1]
            self.parent[vid1] = self.parent[vid0]
        return True
        
class Solution:
    def findRedundantConnection(self, edges):
        N = len(edges)
        uf = UnionFind(N)
        for e0,e1 in edges:
            if not uf.union(e0-1,e1-1):
                return [e0, e1]
