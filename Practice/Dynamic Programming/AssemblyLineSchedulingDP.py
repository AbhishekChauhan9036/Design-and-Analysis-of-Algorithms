def assembly_dp(a, t, e, x):
    n = len(a[0])
    dp1 = [0] * n
    dp2 = [0] * n
    # First station
    dp1[0] = e[0] + a[0][0]
    dp2[0] = e[1] + a[1][0]
    for i in range(1, n):
        dp1[i] = min(dp1[i - 1] + a[0][i], dp2[i - 1] + t[1][i - 1] + a[0][i])
        dp2[i] = min(dp2[i - 1] + a[1][i], dp1[i - 1] + t[0][i - 1] + a[1][i])
    return min(dp1[n - 1] + x[0], dp2[n - 1] + x[1])

a = [[4, 5, 3, 2], [2, 10, 1, 4]]
t = [[7, 4, 5], [9, 2, 8]]
e = [10, 12]
x = [18, 7]
print(assembly_dp(a, t, e, x))

'''
Time Complexity: O(n)
Space Complexity: O(n)
'''