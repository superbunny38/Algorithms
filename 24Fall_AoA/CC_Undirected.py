V = 5
edges = [[1,0],[2,1],[3,4]]

def get_connected_compontents(V,edges):
    undirected_graphs = dict()
    
    for v in range(V):
        undirected_graphs[v] = []
    
    for edge in edges:
        v1,v2 = edge[0],edge[1]
        undirected_graphs[v1].append(v2)
        undirected_graphs[v2].append(v1)
    
    cc = []
    visited = [False for _ in range(V)]
    
    def find(sofar,cur,graph,visited):
        visited[cur] = True
        sofar.append(cur)
        for neighbor in graph[cur]:
            if visited[neighbor] == False:
                sofar = find(sofar,neighbor,graph,visited)
        return sofar
                
    
    for v in range(V):
        if visited[v] == False:
            cc.append(find([],v,undirected_graphs,visited))
    return cc

ccs = get_connected_compontents(V,edges)
print(ccs)