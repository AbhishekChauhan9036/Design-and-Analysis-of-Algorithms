import heapq
graph={
    0:[(4,1),(1,2)],
    1:[(2,2),(5,3)],
    2:[(1,3)],
    3:[]
}

# Dijkstra's Algorithm
def dijkstra(start):
    dist=[float('inf')]*len(graph)
    dist[start]=0
    heap=[(0,start)]

    while heap:
        d,u=heapq.heappop(heap)
        if d>dist[u]:
            continue
        for w,v in graph[u]:
            nd=d+w
            if nd<dist[v]:
                dist[v]=nd
                heapq.heappush(heap,(nd,v))
    return dist

# Floyd-Warshall Algorithm
def floyd_warshall(matrix):
    n=len(matrix)
    dist=[row[:] for row in matrix]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
    return dist

print("Dijkstra:",dijkstra(0))

matrix=[
    [0,4,1,float('inf')],
    [4,0,2,5],
    [1,2,0,1],
    [float('inf'),5,1,0]
]

print("Floyd-Warshall:")
for row in floyd_warshall(matrix):
    print(row)

# Complexity:
# Dijkstra - TC: O((V+E) log V), SC: O(V)
# Floyd-Warshall - TC: O(V^3), SC: O(V^2)

# Dijkstra's Algorithm
'''
1. Set the distance of the start vertex to 0 and all other vertices to infinity.
2. Insert the start vertex into a priority queue with distance 0.
3. While the priority queue is not empty:
      Remove the vertex u with the smallest distance.
      If the distance is greater than the current distance of u:
          Continue.
      For each edge (u, v) with weight w:
          Calculate new distance = distance[u] + w.
          If new distance < distance[v]:
              Update distance[v].
              Insert (new distance, v) into the priority queue.
4. Return the shortest distances from the start vertex.
Dijkstra's - TC: O((V+E) log V), SC: O(V)
'''

# Floyd-Warshall Algorithm
'''
1. Create a distance matrix using the given graph matrix.
2. For each intermediate vertex k:
      For each source vertex i:
          For each destination vertex j:
              Update:
              dist[i][j] = min(dist[i][j],
                               dist[i][k] + dist[k][j])
3. Repeat until all vertices have been considered as intermediate vertices.
4. Return the final distance matrix containing the shortest distances
   between every pair of vertices.
Floyd-Warshall - TC: O(V^3), SC: O(V^2)
'''