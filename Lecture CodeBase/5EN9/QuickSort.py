def partiton(arr, low, high):
    pivot = arr[high]
    i = low -1
    for j in range(low, high):
        if arr[j]<pivot:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quickSort(arr, low, high):
    if low<high:
        pivotindex = partiton(arr, low, high)
        quickSort(arr, low, pivotindex-1)
        quickSort(arr, pivotindex+1, high)

arr = [12, 15, 20, 3, 9, 22, 7, 6]
n = len(arr)
quickSort(arr, 0, n-1)
print(arr)