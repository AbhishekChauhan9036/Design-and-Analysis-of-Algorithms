#include <iostream>
using namespace std;

#define MAX 100

/*=========================================================
    Linear Search

    Time Complexity:
    Best Case    : O(1)
    Average Case : O(n)
    Worst Case   : O(n)

    Space Complexity:
    O(1)
=========================================================*/
int linearSearch(int a[], int n, int key)
{
    int i;

    for(i = 0; i < n; i++)
    {
        if(a[i] == key)
            return i;
    }

    return -1;
}

/*=========================================================
    Binary Search

    Note:
    Array must be sorted in ascending order.

    Time Complexity:
    Best Case    : O(1)
    Average Case : O(log n)
    Worst Case   : O(log n)

    Space Complexity:
    O(1)
=========================================================*/
int binarySearch(int a[], int n, int key)
{
    int low = 0, high = n - 1, mid;

    while(low <= high)
    {
        mid = (low + high) / 2;

        if(a[mid] == key)
            return mid;

        else if(a[mid] < key)
            low = mid + 1;

        else
            high = mid - 1;
    }

    return -1;
}

/*======================= Main =======================*/
int main()
{
    int a[MAX], n, i, key, ch, pos;

    cout << "Enter number of elements: ";
    cin >> n;

    cout << "Enter elements:\n";
    for(i = 0; i < n; i++)
        cin >> a[i];

    cout << "Enter element to search: ";
    cin >> key;

    cout << "\nSearch Algorithms";
    cout << "\n1. Linear Search";
    cout << "\n2. Binary Search";

    cout << "\n\nEnter your choice: ";
    cin >> ch;

    switch(ch)
    {
        case 1:
            pos = linearSearch(a, n, key);
            break;

        case 2:
            pos = binarySearch(a, n, key);
            break;

        default:
            cout << "Invalid Choice";
            return 0;
    }

    if(pos == -1)
        cout << "\nElement Not Found.";
    else
        cout << "\nElement Found at Position " << pos + 1;

    return 0;
}