from collections import deque

def get_connected_components(V, edges):
    undirected_graph = [[] for _ in range(V)]

    for edge in edges:
        v1, v2 = edge[0], edge[1]
        undirected_graph[v1].append(v2)
        undirected_graph[v2].append(v1)

    visited = [False] * V
    cc = []

    def bfs(v, graph, visited):
        queue = deque([v])
        visited[v] = True
        component = []
        while queue:
            node = queue.popleft()
            component.append(node)
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return component

    for v in range(V):
        if not visited[v]:
            cc.append(bfs(v, undirected_graph, visited))

    return cc

# Example usage
V = 5
edges = [[1, 0], [2, 1], [3, 4]]
ccs = get_connected_components(V, edges)
print(ccs)