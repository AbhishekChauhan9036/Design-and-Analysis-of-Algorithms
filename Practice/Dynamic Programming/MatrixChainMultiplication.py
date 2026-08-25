# https://www.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1
class Solution:
    def matrixMultiplication(self, arr):
        n = len(arr)
    
        dp = [[0] * n for _ in range(n)]
    
        for length in range(2, n):
            for i in range(1, n - length + 1):
                j = i + length - 1
    
                dp[i][j] = float('inf')
    
                for k in range(i, j):
                    cost = (dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j])
    
                    if cost < dp[i][j]:
                        dp[i][j] = cost
    
        return dp[1][n - 1]
        
    # Time Complexity: O(n³)
    # Space Complexity: O(n²)