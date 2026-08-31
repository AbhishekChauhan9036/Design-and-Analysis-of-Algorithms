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