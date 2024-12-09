'''
Step 1: Determine an arbitrary vertex as the starting vertex of the MST.
Step 2: Follow steps 3 to 5 till there are vertices that are not included in the MST (known as fringe vertex).
Step 3: Find edges connecting any tree vertex with the fringe vertices.
Step 4: Find the minimum among these edges.
Step 5: Add the chosen edge to the MST if it does not form any cycle.
Step 6: Return the MST and exit
'''
'''
Time Complexity: O(E*log(E)) where E is the number of edges
Auxiliary Space: O(V^2) where V is the number of vertex
'''

import heapq

def tree(V, E, edges):
    # Create an adjacency list representation of the graph
    adj = [[] for _ in range(V)]
    # Fill the adjacency list with edges and their weights
    for i in range(E):
        u, v, wt = edges[i]
        adj[u].append((v, wt))
        adj[v].append((u, wt))
    # Create a priority queue to store edges with their weights
    pq = []
    # Create a visited array to keep track of visited vertices
    visited = [False] * V
    # Variable to store the result (sum of edge weights)
    res = 0
    # Start with vertex 0
    heapq.heappush(pq, (0, 0))
    # Perform Prim's algorithm to find the Minimum Spanning Tree
    while pq:
        wt, u = heapq.heappop(pq)
        if visited[u]:
            continue  
            # Skip if the vertex is already visited
        res += wt  
        # Add the edge weight to the result
        visited[u] = True  
        # Mark the vertex as visited
        # Explore the adjacent vertices
        for v, weight in adj[u]:
            if not visited[v]:
                heapq.heappush(pq, (weight, v))  
                # Add the adjacent edge to the priority queue
    return res  
  # Return the sum of edge weights of the Minimum Spanning Tree
if __name__ == "__main__":
    graph = [[0, 1, 5],
             [1, 2, 3],
             [0, 2, 1]]
    # Function call
    print(tree(3, 3, graph))