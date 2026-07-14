"""
=========================================================
                    Shell Sort

Time Complexity:
Best Case    : O(n log n)
Average Case : O(n^1.3)   # Approximate, depends on gap sequence
Worst Case   : O(n²)

Space Complexity:
O(1)

Stable:
No

In-Place:
Yes
=========================================================
"""

def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            # Shift earlier gap-sorted elements up until
            # the correct location for arr[i] is found
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        gap //= 2


def print_array(arr):
    print(*arr)


# Main Program
n = int(input("Enter the size of the array: "))

arr = list(map(int, input(f"Enter {n} elements: ").split()))

print("Original Array:", end=" ")
print_array(arr)

shell_sort(arr)

print("Sorted Array:", end=" ")
print_array(arr)