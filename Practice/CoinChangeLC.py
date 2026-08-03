# https://leetcode.com/problems/coin-change/
class Solution:
    def coinChange(self, coins, amount):
        # dp[i] = Minimum coins needed to make amount i
        dp = [amount + 1] * (amount + 1)

        # Base case
        dp[0] = 0

        # Fill the DP array
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        # If amount cannot be formed
        if dp[amount] == amount + 1:
            return -1

        return dp[amount]

        '''
        Time Complexity
        O(N * Amount)
        Space Complexity
        O(Amount)
        '''