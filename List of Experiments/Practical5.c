#include <stdio.h>

#define MAX 100

/*=========================================================
    0/1 Knapsack using Dynamic Programming

    Time Complexity:
    Best Case    : O(n * W)
    Average Case : O(n * W)
    Worst Case   : O(n * W)

    Space Complexity:
    O(n * W)

    Where:
    n = Number of items
    W = Maximum capacity of knapsack
=========================================================*/

int max(int a, int b)
{
    if(a > b)
        return a;
    else
        return b;
}

int knapsack(int wt[], int val[], int n, int W)
{
    int dp[MAX][MAX];
    int i, w;

    // Initialize first row and first column
    for(i = 0; i <= n; i++)
        dp[i][0] = 0;

    for(w = 0; w <= W; w++)
        dp[0][w] = 0;

    // Fill DP Table
    for(i = 1; i <= n; i++)
    {
        for(w = 1; w <= W; w++)
        {
            if(wt[i-1] <= w)
            {
                dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]],
                               dp[i-1][w]);
            }
            else
            {
                dp[i][w] = dp[i-1][w];
            }
        }
    }

    return dp[n][W];
}

/*======================= Main =======================*/
int main()
{
    int n, W;
    int wt[MAX], val[MAX];
    int i;

    printf("Enter number of items: ");
    scanf("%d", &n);

    printf("Enter weights:\n");
    for(i = 0; i < n; i++)
        scanf("%d", &wt[i]);

    printf("Enter values:\n");
    for(i = 0; i < n; i++)
        scanf("%d", &val[i]);

    printf("Enter knapsack capacity: ");
    scanf("%d", &W);

    printf("\nMaximum Profit = %d", knapsack(wt, val, n, W));

    return 0;
}