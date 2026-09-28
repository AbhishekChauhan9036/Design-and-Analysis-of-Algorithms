'''
Step 1: Start with a cost matrix of workers and jobs.
Step 2: Assign the first worker to an available job.
Step 3: Calculate the current cost and lower bound.
Step 4: Select the node with the minimum bound.
Step 5: Assign the next worker to an unassigned job.
Step 6: If the bound is greater than the current minimum cost, discard the node.
Step 7: Continue until all workers are assigned.
Step 8: The assignment with minimum cost is the optimal solution.

Time Complexity: O(N!)
Space Complexity: O(N²)
'''
N=3
cost=[[9,2,7],
      [6,4,3],
      [5,8,1]]
best=float('inf')
bestpath=[]
def assign(row,used,total,path):
    global best,bestpath
    if row==N:
        if total<best:
            best=total
            bestpath=path[:]
        return
    if total>=best:
        return
    for col in range(N):
        if not used[col]:
            used[col]=True
            path.append(col)
            assign(row+1,used,total+cost[row][col],path)
            path.pop()
            used[col]=False
assign(0,[False]*N,0,[])
print("Minimum Cost:",best)
print("Assignment:",bestpath)