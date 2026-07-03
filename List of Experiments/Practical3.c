#include <stdio.h>

#define MAX 100

/*=========================================================
    Heap Sort (Max Heap)

    Time Complexity:
    Best Case    : O(n log n)
    Average Case : O(n log n)
    Worst Case   : O(n log n)

    Space Complexity:
    O(1)

    Note:
    Heap Sort first builds a Max Heap and then repeatedly
    swaps the root (largest element) with the last element.
=========================================================*/

// Function to heapify a subtree
void heapify(int a[], int n, int i)
{
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;
    int temp;

    if(left < n && a[left] > a[largest])
        largest = left;

    if(right < n && a[right] > a[largest])
        largest = right;

    if(largest != i)
    {
        temp = a[i];
        a[i] = a[largest];
        a[largest] = temp;

        heapify(a, n, largest);
    }
}

// Heap Sort Function
void heapSort(int a[], int n)
{
    int i, temp;

    // Build Max Heap
    for(i = n/2 - 1; i >= 0; i--)
        heapify(a, n, i);

    // Extract elements one by one
    for(i = n-1; i > 0; i--)
    {
        temp = a[0];
        a[0] = a[i];
        a[i] = temp;

        heapify(a, i, 0);
    }
}

// Display Array
void printArray(int a[], int n)
{
    int i;

    printf("\nSorted Array:\n");

    for(i = 0; i < n; i++)
        printf("%d ", a[i]);

    printf("\n");
}

// Main Function
int main()
{
    int a[MAX], n, i;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    printf("Enter elements:\n");
    for(i = 0; i < n; i++)
        scanf("%d", &a[i]);

    heapSort(a, n);

    printArray(a, n);

    return 0;
}