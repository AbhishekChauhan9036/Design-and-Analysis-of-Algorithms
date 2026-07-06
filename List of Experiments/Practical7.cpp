#include <iostream>
using namespace std;

#define MAX 100
#define INF 999999

/*=========================================================
    Coin Change (Making Change) using Dynamic Programming

    Time Complexity:
    Best Case    : O(n * Amount)
    Average Case : O(n * Amount)
    Worst Case   : O(n * Amount)

    Space Complexity:
    O(Amount)

    Where:
    n = Number of coin denominations
    Amount = Total amount to make

    Note:
    Finds the minimum number of coins required
    to make the given amount.
=========================================================*/

int min(int a, int b)
{
    if(a < b)
        return a;
    else
        return b;
}

int coinChange(int coin[], int n, int amount)
{
    int dp[MAX];
    int i, j;

    // Initialize DP array
    dp[0] = 0;

    for(i = 1; i <= amount; i++)
        dp[i] = INF;

    // Fill DP table
    for(i = 1; i <= amount; i++)
    {
        for(j = 0; j < n; j++)
        {
            if(coin[j] <= i)
            {
                dp[i] = min(dp[i], dp[i - coin[j]] + 1);
            }
        }
    }

    if(dp[amount] == INF)
        return -1;

    return dp[amount];
}

/*======================= Main =======================*/
int main()
{
    int coin[MAX];
    int n, amount, i, ans;

    cout << "Enter number of coin denominations: ";
    cin >> n;

    cout << "Enter coin values:\n";
    for(i = 0; i < n; i++)
        cin >> coin[i];

    cout << "Enter amount: ";
    cin >> amount;

    ans = coinChange(coin, n, amount);

    if(ans == -1)
        cout << "\nChange cannot be made.";
    else
        cout << "\nMinimum Coins Required = " << ans;

    return 0;
}