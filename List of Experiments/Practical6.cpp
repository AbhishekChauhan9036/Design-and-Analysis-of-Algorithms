#include <iostream>
using namespace std;

#define MAX 100
#define INF 999999

/*=========================================================
    Matrix Chain Multiplication using Dynamic Programming

    Time Complexity:
    Best Case    : O(n^3)
    Average Case : O(n^3)
    Worst Case   : O(n^3)

    Space Complexity:
    O(n^2)

    Where:
    n = Number of matrices

    Note:
    Finds the minimum number of scalar multiplications
    required to multiply a chain of matrices.
=========================================================*/

int matrixChain(int p[], int n)
{
    int dp[MAX][MAX];
    int i, j, k, l, q;

    // Cost is 0 when multiplying one matrix
    for(i = 1; i <= n; i++)
        dp[i][i] = 0;

    // l = Chain Length
    for(l = 2; l <= n; l++)
    {
        for(i = 1; i <= n - l + 1; i++)
        {
            j = i + l - 1;
            dp[i][j] = INF;

            for(k = i; k < j; k++)
            {
                q = dp[i][k] +
                    dp[k + 1][j] +
                    p[i - 1] * p[k] * p[j];

                if(q < dp[i][j])
                    dp[i][j] = q;
            }
        }
    }

    return dp[1][n];
}

/*======================= Main =======================*/
int main()
{
    int n, i;
    int p[MAX];

    cout << "Enter number of matrices: ";
    cin >> n;

    cout << "Enter " << n + 1 << " dimensions:\n";

    for(i = 0; i <= n; i++)
        cin >> p[i];

    cout << "\nMinimum Multiplications = " << matrixChain(p, n);

    return 0;
}