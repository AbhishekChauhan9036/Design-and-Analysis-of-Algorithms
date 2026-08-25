"""
=========================================================
                 Binary Search

Time Complexity:
Best Case    : O(1)
Average Case : O(log n)
Worst Case   : O(log n)

Space Complexity:
O(1)

Stable:
Not Applicable

In-Place:
Yes

Note:
The array must be sorted before performing Binary Search.
=========================================================
"""

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Main Program
n = int(input("Enter the size of the sorted array: "))

arr = list(map(int, input(f"Enter {n} sorted elements: ").split()))

key = int(input("Enter the element to search: "))

index = binary_search(arr, key)

if index != -1:
    print(f"Element found at index {index}")
else:
    print("Element not found.")