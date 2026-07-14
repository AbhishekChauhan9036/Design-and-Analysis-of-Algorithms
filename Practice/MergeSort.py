"""
=========================================================
                    Merge Sort

Time Complexity:
Best Case    : O(n log n)
Average Case : O(n log n)
Worst Case   : O(n log n)

Space Complexity:
O(n)

Stable:
Yes

In-Place:
No
=========================================================
"""

def merge(arr, left, mid, right):
    # Create temporary subarrays
    left_subarray = arr[left:mid + 1]
    right_subarray = arr[mid + 1:right + 1]

    i = 0
    j = 0
    k = left

    # Merge the temporary arrays back into arr
    while i < len(left_subarray) and j < len(right_subarray):
        if left_subarray[i] <= right_subarray[j]:
            arr[k] = left_subarray[i]
            i += 1
        else:
            arr[k] = right_subarray[j]
            j += 1
        k += 1

    # Copy any remaining elements of left_subarray
    while i < len(left_subarray):
        arr[k] = left_subarray[i]
        i += 1
        k += 1

    # Copy any remaining elements of right_subarray
    while j < len(right_subarray):
        arr[k] = right_subarray[j]
        j += 1
        k += 1


def merge_sort(arr, left, right):
    if left < right:
        mid = left + (right - left) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        merge(arr, left, mid, right)


def print_array(arr):
    print(*arr)


# Main Program
n = int(input("Enter the size of the array: "))

arr = list(map(int, input(f"Enter {n} elements: ").split()))

print("\nOriginal Array:", end=" ")
print_array(arr)

merge_sort(arr, 0, n - 1)

print("Sorted Array:", end=" ")
print_array(arr)