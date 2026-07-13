#include <iostream>
using namespace std;

/**
 * =========================================================
 *                  Linear Search
 *
 * Time Complexity:
 * Best Case    : O(1)
 * Average Case : O(n)
 * Worst Case   : O(n)
 *
 * Space Complexity:
 * O(1)
 *
 * Stable:
 * Not Applicable
 *
 * In-Place:
 * Yes
 * =========================================================
 */

int linearSearch(int arr[], int n, int key) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == key)
            return i;
    }
    return -1;
}

int main() {
    int n;

    cout << "Enter the size of the array: ";
    cin >> n;

    int arr[n];

    cout << "Enter " << n << " elements: ";
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    int key;
    cout << "Enter the element to search: ";
    cin >> key;

    int index = linearSearch(arr, n, key);

    if (index != -1)
        cout << "Element found at index " << index << endl;
    else
        cout << "Element not found." << endl;

    return 0;
}