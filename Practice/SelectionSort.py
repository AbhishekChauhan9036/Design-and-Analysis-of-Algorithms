"""
=========================================================
                  Selection Sort

Time Complexity:
Best Case    : O(n²)
Average Case : O(n²)
Worst Case   : O(n²)

Space Complexity:
O(1)

Stable:
No

In-Place:
Yes
=========================================================
"""

def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        # Find the index of the minimum element
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap if a smaller element is found
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]


def print_array(arr):
    print(*arr)


# Main Program
n = int(input("Enter the size of the array: "))

arr = list(map(int, input(f"Enter {n} elements: ").split()))

print("\nOriginal Array:", end=" ")
print_array(arr)

selection_sort(arr)

print("Sorted Array:", end=" ")
print_array(arr)