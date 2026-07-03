#include <stdio.h>

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

    printf("Enter a number: ");
    scanf("%d", &n);

    printf("\nFactorial Methods");
    printf("\n1. Iterative Method");
    printf("\n2. Recursive Method");

    printf("\n\nEnter your choice: ");
    scanf("%d", &ch);

    switch(ch)
    {
        case 1:
            ans = iterativeFactorial(n);
            printf("\nFactorial = %lld", ans);
            break;

        case 2:
            ans = recursiveFactorial(n);
            printf("\nFactorial = %lld", ans);
            break;

        default:
            printf("Invalid Choice");
    }

    return 0;
}