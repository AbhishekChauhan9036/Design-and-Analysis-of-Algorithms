def knapsack_dp(weights, values, capacity):
    n = len(weights)

    # DP table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            # Current item can be included
            if weights[i - 1] <= w:
                include = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                exclude = dp[i - 1][w]

                dp[i][w] = max(include, exclude)

            # Current item cannot be included
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Example
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

print("Maximum Value:", knapsack_dp(weights, values, capacity))


'''
Time: O(n × W)
Space: O(n × W)

Where:
n = number of items
W = knapsack capacity
'''