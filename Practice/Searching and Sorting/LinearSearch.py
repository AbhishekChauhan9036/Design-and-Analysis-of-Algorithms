"""
=========================================================
                  Linear Search

Time Complexity:
Best Case    : O(1)
Average Case : O(n)
Worst Case   : O(n)

Space Complexity:
O(1)

Stable:
Not Applicable

In-Place:
Yes
=========================================================
"""

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


# Main Program
n = int(input("Enter the size of the array: "))

arr = list(map(int, input(f"Enter {n} elements: ").split()))

key = int(input("Enter the element to search: "))

index = linear_search(arr, key)

if index != -1:
    print(f"Element found at index {index}")
else:
    print("Element not found.")