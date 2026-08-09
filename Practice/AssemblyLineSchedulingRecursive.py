def assembly_recursive(a, t, e, x):
    n = len(a[0])
    def solve(line, i):
        # First station
        if i == 0:
            return e[line] + a[line][0]
        # Stay on same line
        stay = solve(line, i - 1) + a[line][i]
        # Switch from other line
        other = 1 - line
        switch = solve(other, i - 1) + t[other][i - 1] + a[line][i]
        return min(stay, switch)
    return min(solve(0, n - 1) + x[0], solve(1, n - 1) + x[1])

a = [[4, 5, 3, 2], [2, 10, 1, 4]]
t = [[7, 4, 5], [9, 2, 8]]
e = [10, 12]
x = [18, 7]
print(assembly_recursive(a, t, e, x))
'''
Time Complexity: O(2^n)
Space Complexity: O(n) (recursion stack)
'''