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

'''
                         lcs(7,5)
                       X[6]=B, Y[4]=B
                            |
                         MATCH
                            |
                         lcs(6,4)
                    X[5]=A, Y[3]=A
                            |
                         MATCH
                            |
                         lcs(5,3)
                    X[4]=D, Y[2]=C
                         MISMATCH
                       /           \
                  lcs(4,3)       lcs(5,2)
                 D vs C          D vs A
                MISMATCH        MISMATCH
                /    \           /     \
           lcs(3,3) lcs(4,2) lcs(4,2) lcs(5,1)
             ...       ...       ...      ...
'''