'''
Complexity Analysis:
Time Complexity: Tarjan's algorithm has a time complexity of O(V + E), where V is the number of vertices and E is the number of edges in the graph.
Space Complexity: The space complexity of the algorithm is O(V), where V is the number of vertices, due to the stack used in DFS traversal
'''
class TarjanSCC:
    def __init__(self, graph):
        self.time = 0
        self.stack = []
        self.low_link = {}
        self.visited = set()
        self.sccs = []
        self.graph = graph
    
    def dfs(self,cur_node):
        self.low_link[cur_node] = self.time
        self.time +=1
        self.stack.append(cur_node)
        self.visited.add(cur_node)
        
        for neighbor in self.graph[cur_node]:
            if neighbor not in self.low_link:
                self.dfs(neighbor)
            elif neighbor in self.stack:
                pass
            else:
                continue
            self.low_link[cur_node] = min(self.low_link[cur_node],self.low_link[neighbor])
        
        if self.low_link[cur_node] == cur_node:
            cur_sccs = []
            while True:
                u = self.stack.pop()
                cur_sccs.append(u)
                if u == cur_node:
                    break
            self.sccs.append(cur_sccs)
            
                
    
    def find_sccs(self):
        for key in self.graph:
            if key not in self.low_link:
                self.dfs(key)
        
        return self.sccs
    
graph = dict()
for _ in range(8):
    graph[_] = []

edges = [[0,1],[1,2],[2,3],[2,4],[3,0],[4,5],[5,6],[6,4],[6,7]]
for edge in edges:
    v1,v2 = edge[0],edge[1]
    graph[v1].append(v2)

tarjan = TarjanSCC(graph)
sccs = tarjan.find_sccs()
print(sccs)