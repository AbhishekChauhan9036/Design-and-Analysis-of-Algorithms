def fun(n):
    if n == 0 or n == 1:
        return n

    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

ans = fun(4)
print(ans)
"""
TC : O(n)
SC : O(n)
"""
