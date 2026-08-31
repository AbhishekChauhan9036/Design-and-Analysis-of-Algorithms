import heapq
# Graph represented as (weight, vertex1, vertex2)
edges = [
    (1, 0, 1),
    (2, 0, 2),
    (3, 1, 2),
    (4, 1, 3),
    (5, 2, 3)
]
vertices = 4

# Kruskal's Algorithm
def kruskal():
    parent = list(range(vertices))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    mst = []
    for weight, u, v in sorted(edges):
        pu, pv = find(u), find(v)
        if pu != pv:
            parent[pu] = pv
            mst.append((u, v, weight))
    return mst


# Prim's Algorithm
def prim():
    graph = [[] for _ in range(vertices)]
    for weight, u, v in edges:
        graph[u].append((weight, v))
        graph[v].append((weight, u))
    visited = [False] * vertices
    heap = [(0, 0)]
    mst = []
    while heap:
        weight, u = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        if weight != 0:
            mst.append((u, weight))
        for w, v in graph[u]:
            if not visited[v]:
                heapq.heappush(heap, (w, v))
    return mst

print("Kruskal's MST:", kruskal())
print("Prim's MST:", prim())

# Complexity:
# Kruskal's - TC: O(E log E), SC: O(V)
# Prim's    - TC: O(E log V), SC: O(V + E)