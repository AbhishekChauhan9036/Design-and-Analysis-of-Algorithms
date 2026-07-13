#include <iostream>
using namespace std;

/**
 * =========================================================
 *                  Binary Search
 *
 * Time Complexity:
 * Best Case    : O(1)
 * Average Case : O(log n)
 * Worst Case   : O(log n)
 *
 * Space Complexity:
 * O(1)
 *
 * Stable:
 * Not Applicable
 *
 * In-Place:
 * Yes
 *
 * Note:
 * The array must be sorted before performing Binary Search.
 * =========================================================
 */

int binarySearch(int arr[], int n, int key) {
    int low = 0, high = n - 1;

    while (low <= high) {
        int mid = low + (high - low) / 2;

        if (arr[mid] == key)
            return mid;
        else if (arr[mid] < key)
            low = mid + 1;
        else
            high = mid - 1;
    }

    return -1;
}

int main() {
    int n;

    cout << "Enter the size of the sorted array: ";
    cin >> n;

    int arr[n];

    cout << "Enter " << n << " sorted elements: ";
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    int key;
    cout << "Enter the element to search: ";
    cin >> key;

    int index = binarySearch(arr, n, key);

    if (index != -1)
        cout << "Element found at index " << index << endl;
    else
        cout << "Element not found." << endl;

    return 0;
}