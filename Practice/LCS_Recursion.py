def lcs(X, Y, m, n):
    # Base case
    if m == 0 or n == 0:
        return 0
    # If characters match
    if X[m - 1] == Y[n - 1]:
        return 1 + lcs(X, Y, m - 1, n - 1)
    # If characters don't match
    else:
        return max(lcs(X, Y, m - 1, n),lcs(X, Y, m, n - 1))

X = "ABCBDAB"
Y = "BDCAB"
m = len(X)
n = len(Y)
print("Length of LCS:", lcs(X, Y, m, n))

'''
Time Complexity: O(2^(m+n)) | O(2)^n
Space Complexity: O(m+n)
'''