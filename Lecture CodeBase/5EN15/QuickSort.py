def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j]<pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1

def quickSort(arr, low, high):
    if low<high:
        pivotind = partition(arr, low, high)
        quickSort(arr, low, pivotind-1)
        quickSort(arr, pivotind+1, high)

arr = [23, 6, 90, 21, 80, 22, 11, 67]
n = len(arr)
quickSort(arr, 0, n-1)
print(arr)
'''
TC -
    Best Case: O(n log n)
    Average Case: O(n log n)
    Worst Case: O(n)^2

SC : O(log n)
'''