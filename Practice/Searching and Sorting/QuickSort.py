"""
=========================================================
                    Quick Sort

Time Complexity:
Best Case    : O(n log n)
Average Case : O(n log n)
Worst Case   : O(n²)

Space Complexity:
Best Case    : O(log n)
Average Case : O(log n)
Worst Case   : O(n)

Stable:
No

In-Place:
Yes
=========================================================
"""

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            # Swap elements
            arr[i], arr[j] = arr[j], arr[i]

    # Place the pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)

        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


def print_array(arr):
    print(*arr)


# Main Program
n = int(input("Enter the size of the array: "))

arr = list(map(int, input(f"Enter {n} elements: ").split()))

print("\nOriginal Array:", end=" ")
print_array(arr)

quick_sort(arr, 0, n - 1)

print("Sorted Array:", end=" ")
print_array(arr)