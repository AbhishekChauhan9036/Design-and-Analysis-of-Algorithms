#include <iostream>
using namespace std;

/*=========================================================
    Iterative Factorial

    Time Complexity:
    Best Case    : O(n)
    Average Case : O(n)
    Worst Case   : O(n)

    Space Complexity:
    O(1)
=========================================================*/
long long iterativeFactorial(int n)
{
    int i;
    long long fact = 1;

    for(i = 1; i <= n; i++)
    {
        fact = fact * i;
    }

    return fact;
}

/*=========================================================
    Recursive Factorial

    Time Complexity:
    Best Case    : O(n)
    Average Case : O(n)
    Worst Case   : O(n)

    Space Complexity:
    O(n)

    Note:
    Recursive method uses function call stack.
=========================================================*/
long long recursiveFactorial(int n)
{
    if(n == 0 || n == 1)
        return 1;

    return n * recursiveFactorial(n - 1);
}

/*======================= Main =======================*/
int main()
{
    int n, ch;
    long long ans;

    cout << "Enter a number: ";
    cin >> n;

    cout << "\nFactorial Methods";
    cout << "\n1. Iterative Method";
    cout << "\n2. Recursive Method";

    cout << "\n\nEnter your choice: ";
    cin >> ch;

    switch(ch)
    {
        case 1:
            ans = iterativeFactorial(n);
            cout << "\nFactorial = " << ans;
            break;

        case 2:
            ans = recursiveFactorial(n);
            cout << "\nFactorial = " << ans;
            break;

        default:
            cout << "Invalid Choice";
    }

    return 0;
}