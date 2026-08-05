# https://www.geeksforgeeks.org/problems/number-of-coins1824/1
class Solution:
    def minCoins(self, coins, amt):
        dp = [float('inf')] * (amt + 1)
        dp[0] = 0

        for cur in range(1, amt + 1):
            for coin in coins:
                if cur >= coin:
                    dp[cur] = min(dp[cur], dp[cur - coin] + 1)

        return dp[amt] if dp[amt] != float('inf') else -1

'''
TC: O(n × amt)
SC: O(amt)
'''