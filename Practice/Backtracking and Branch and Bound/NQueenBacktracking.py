'''
Step 1: Start with an empty N × N chessboard.
Step 2: Place the queen from the first row.
Step 3: Try each column in the current row.
Step 4: Check whether the position is safe:
    No queen in the same column.
    No queen on either diagonal.
Step 5: If safe, place the queen and move to the next row.
Step 6: If all N queens are placed, print the solution.
Step 7: If no safe position is found, remove the previous queen and backtrack.
Step 8: Try the next position until all solutions are found.
Time Complexity: O(N!) approximately
Space Complexity: O(N²) + O(N) recursion stack.
'''
N=4
board=[[0]*N for _ in range(N)]
def nqueen(row):
    if row==N:
        for r in board:
            print(r)
        print()
        return
    
    for col in range(N):
        safe=True
        for i in range(row):
            for j in range(N):
                if board[i][j]==1:
                    if j==col or abs(i-row)==abs(j-col):
                        safe=False
        if safe:
            board[row][col]=1
            nqueen(row+1)
            board[row][col]=0
nqueen(0)