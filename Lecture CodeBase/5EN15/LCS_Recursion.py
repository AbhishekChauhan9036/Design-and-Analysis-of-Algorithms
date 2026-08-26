def lcs(X, Y, m, n):
    if m == 0 or n==0:
        return 0
    if X[m-1] == Y[n-1]:
        return 1+lcs(X, Y, m-1, n-1)
    else:
        return max(lcs(X, Y, m-1, n), lcs(X, Y, m, n-1))

X = "RISHABH"
Y = "SHUBHI"
m = len(X)
n = len(Y)
print(lcs(X, Y, m, n))
'''
TC : O(2)^m+n
SC : O(m+n)
'''