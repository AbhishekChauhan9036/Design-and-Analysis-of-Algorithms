# https://www.geeksforgeeks.org/problems/coin-change2448/1

class Solution:
    def count(self, coins, sum):
        # dp[i] = Number of ways to make amount i
        dp = [0] * (sum + 1)
        dp[0] = 1  # One way to make sum 0

        # Process each coin
        for coin in coins:
            for amount in range(coin, sum + 1):
                dp[amount] += dp[amount - coin]

        return dp[sum]
        
        
'''
TC : O(n * sum)
SC : O(sum)
'''