def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1)+fib(n-2)

ans = fib(6)
print(ans)
'''
TC : O(2)^n
SC : O(log n)
'''


def fun(n):
    if n==0 or n==1:
        return n

    dp = [0]*(n+1)
    dp[0],dp[1] = 0,1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

a = fun(6)
print(a)
'''
TC : O(n)
SC : O(n)
'''