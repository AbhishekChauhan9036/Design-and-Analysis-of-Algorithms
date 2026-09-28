'''
Step 1: Start with a graph and a set of available colors.
Step 2: Start coloring from the first vertex.
Step 3: Try each color for the current vertex.
Step 4: Check whether the color is safe.
    No adjacent vertex has the same color.
Step 5: If safe, assign the color and move to the next vertex.
Step 6: If all vertices are colored, print the solution.
Step 7: If no color is safe, remove the color and backtrack.
Step 8: Try the next color until a valid solution is found.

Time Complexity: O(M^N)
Space Complexity: O(N) recursion stack.
'''
N=4
M=3
graph=[[0,1,1,1],
       [1,0,1,0],
       [1,1,0,1],
       [1,0,1,0]]
color=[0]*N
def graphcolor(v):
    if v==N:
        print(color)
        return True
    for c in range(1,M+1):
        safe=True
        for i in range(N):
            if graph[v][i]==1 and color[i]==c:
                safe=False
        if safe:
            color[v]=c
            if graphcolor(v+1):
                return True
            color[v]=0
    return False
graphcolor(0)