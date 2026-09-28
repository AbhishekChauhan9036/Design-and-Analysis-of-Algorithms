'''
Step 1: Start from the first city.
Step 2: Add the current city to the path.
Step 3: Try each unvisited city.
Step 4: Calculate the cost of moving to the next city.
Step 5: Move to the next city and continue.
Step 6: If all cities are visited, return to the starting city.
Step 7: Compare the total cost with the minimum cost.
Step 8: Remove the city and backtrack to try another path.

Time Complexity: O(N!)
Space Complexity: O(N) recursion stack.
'''
N=4
cost=[[0,10,15,20],
      [10,0,35,25],
      [15,35,0,30],
      [20,25,30,0]]
visited=[False]*N
path=[0]
visited[0]=True
mincost=float('inf')
def tsp(city,total):
    global mincost
    if len(path)==N:
        total+=cost[city][0]
        mincost=min(mincost,total)
        return
    for i in range(N):
        if not visited[i]:
            visited[i]=True
            path.append(i)
            tsp(i,total+cost[city][i])
            path.pop()
            visited[i]=False
tsp(0,0)
print("Minimum Cost:",mincost)