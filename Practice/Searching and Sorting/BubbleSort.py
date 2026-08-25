"""
=========================================================
                    Bubble Sort

Time Complexity:
Best Case    : O(n)      # Already sorted (with optimization)
Average Case : O(n²)
Worst Case   : O(n²)

Space Complexity:
O(1)

Stable:
Yes

In-Place:
Yes
=========================================================
"""

def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        swapped = False

        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap adjacent elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swapping occurred, array is already sorted
        if not swapped:
            break


def print_array(arr):
    print(*arr)


# Main Program
n = int(input("Enter the size of the array: "))

arr = list(map(int, input(f"Enter {n} elements: ").split()))

print("\nOriginal Array:", end=" ")
print_array(arr)

bubble_sort(arr)

print("Sorted Array:", end=" ")
print_array(arr)