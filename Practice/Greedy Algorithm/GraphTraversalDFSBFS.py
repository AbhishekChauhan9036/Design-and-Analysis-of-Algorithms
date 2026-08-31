from collections import deque

graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 4],
    3: [1],
    4: [2]
}

# DFS
def dfs(node, visited=None):
    if visited is None:
        visited = set()

    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited)


# BFS
def bfs(start):
    visited = {start}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


print("DFS:", end=" ")
dfs(0)

print("\nBFS:", end=" ")
bfs(0)

# Complexity:
# DFS - TC: O(V + E), SC: O(V)
# BFS - TC: O(V + E), SC: O(V)