def assemblyLine(a, t, e, x):
    n = len(a[0])
    def solve(line , i):
        if i == 0:
            return e[line] + a[line][0]
        stay = solve(line, i-1)+a[line][i]
        other = 1 - line
        switch = solve(other, i-1)+ t[other][i-1]+a[line][i]
        return min(stay, switch)
    return min(solve(0, n-1)+x[0], solve(1, n-1)+x[1])

a = [[1,2],[3,4]]
t = [[4,5],[3,2]]
e = [3,4]
x = [7,8]
print(assemblyLine(a, t, e, x))
'''
TC: O(2)^n
SC : O(n)
'''