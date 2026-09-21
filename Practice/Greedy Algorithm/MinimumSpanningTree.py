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


# Kruskal's Algorithm
"""
1. Sort all edges in increasing order of weight.
2. Create a separate set for each vertex.
3. For each edge (u, v) in sorted order:
      If u and v belong to different sets:
          Add (u, v) to MST.
          Union the sets of u and v.
4. Repeat until MST contains V - 1 edges.
5. Return MST.

Kruskal's - TC: O(E log E), SC: O(V)
"""


# Prim's Algorithm
'''
1. Select any starting vertex s.
2. Set key[s] = 0 and all other keys = ∞.
3. Insert (0, s) into Min-Heap.
4. While Min-Heap is not empty:
      u = Extract-Min()
      Mark u as visited.
5. For each adjacent vertex v of u:
      If v is unvisited and weight(u,v) < key[v]:
          key[v] = weight(u,v)
          parent[v] = u
          Insert (key[v], v) into Min-Heap.
6. Add all parent edges to MST.
7. Return MST.

TC: O(E log V), SC: O(V + E)
'''