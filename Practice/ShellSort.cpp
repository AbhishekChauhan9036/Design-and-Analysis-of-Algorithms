#include <iostream>
using namespace std;

void shellSort(int arr[], int n) {
    for (int gap = n / 2; gap > 0; gap /= 2) {
        for (int i = gap; i < n; i++) {
            int temp = arr[i];
            int j = i;

            while (j >= gap && arr[j - gap] > temp) {
                arr[j] = arr[j - gap];
                j -= gap;
            }

            arr[j] = temp;
        }
    }
}

void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;
}

int main() {
    int n;

    cout << "Enter the size of the array: ";
    cin >> n;

    int arr[n];

    cout << "Enter " << n << " elements: ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    cout << "Original Array: ";
    printArray(arr, n);

    shellSort(arr, n);

    cout << "Sorted Array: ";
    printArray(arr, n);

    return 0;
}


/**
 * =========================================================
 *                    Shell Sort
 *
 * Time Complexity:
 * Best Case    : O(n log n)
 * Average Case : O(n^1.3)   // Approximate, depends on gap sequence
 * Worst Case   : O(n^2)
 *
 * Space Complexity:
 * O(1)
 *
 * Stable:
 * No
 *
 * In-Place:
 * Yes
 * =========================================================
 */