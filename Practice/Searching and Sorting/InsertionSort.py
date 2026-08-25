"""
=========================================================
                  Insertion Sort

Time Complexity:
Best Case    : O(n)
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

def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


def print_array(arr):
    print(*arr)


# Main Program
n = int(input("Enter the size of the array: "))

arr = list(map(int, input(f"Enter {n} elements: ").split()))

print("\nOriginal Array:", end=" ")
print_array(arr)

insertion_sort(arr)

print("Sorted Array:", end=" ")
print_array(arr)