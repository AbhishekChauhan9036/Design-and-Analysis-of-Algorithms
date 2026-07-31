def partition(arr, low, high):
    pivot = arr[high]
    i = low -1
    for j in range(low, high):
        if arr[j]<pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high],arr[i+1]
    return i+1

def quickSort(arr, low, high):
    if low<high:
        pivotindex = partition(arr, low, high)
        quickSort(arr, low, pivotindex-1)
        quickSort(arr, pivotindex+1, high)

arr = [2,5,7,18,0,3,2,6,8]
n = len(arr)
quickSort(arr, 0, n-1)
print(arr)
'''
TC :
    Best Case : O(n log n)
    Average Case: O(n log n)
    Worst Case: O(n)^2

SC: O(log n)
'''