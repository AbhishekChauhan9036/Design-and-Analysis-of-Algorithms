'''
Step 1: Start with a graph and select the first vertex.
Step 2: Add the first vertex to the path.
Step 3: Try each unvisited adjacent vertex.
Step 4: Check whether the vertex can be added to the path.
    It must be connected and not already visited.
Step 5: If safe, add the vertex and move to the next vertex.
Step 6: If all vertices are added, check the last vertex connects to the first.
Step 7: If not, remove the last vertex and backtrack.
Step 8: Try the next available vertex until a cycle is found.

Time Complexity: O(N!)
Space Complexity: O(N) recursion stack.
'''
N=5
graph=[[0,1,0,1,0],
       [1,0,1,1,1],
       [0,1,0,0,1],
       [1,1,0,0,1],
       [0,1,1,1,0]]
path=[0]
def hamiltonian(v):
    if len(path)==N:
        return graph[path[-1]][path[0]]==1
    for i in range(1,N):
        if graph[v][i]==1 and i not in path:
            path.append(i)
            if hamiltonian(i):
                return True
            path.pop()
    return False

if hamiltonian(0):
    path.append(path[0])
    print(path)
else:
    print("No Hamiltonian Cycle")