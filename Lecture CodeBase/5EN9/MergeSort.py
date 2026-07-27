def merge(arr, left, mid, right):
    leftsubArray = arr[left:mid+1]
    rightsubArray = arr[mid+1:right+1]
    i = 0
    j = 0
    k = left
    while i<len(leftsubArray) and j<len(rightsubArray):
        if leftsubArray[i] <=rightsubArray[j]:
            arr[k] = leftsubArray[i]
            i+=1
        else:
            arr[k] = rightsubArray[j]
            j+=1
        k+=1

    while i<len(leftsubArray):
        arr[k] = leftsubArray[i]
        i+=1
        k+=1

    while j<len(rightsubArray):
        arr[k] = rightsubArray[j]
        j+=1
        k+=1

def mergeSort(arr, left, right):
    if left<right:
        mid = (left + right)//2
        mergeSort(arr, left, mid)
        mergeSort(arr, mid+1, right)
        merge(arr, left, mid, right)

arr = [12, 15, 20, 3, 9, 22, 7, 2]
n = len(arr)
mergeSort(arr, 0, n-1)
print(arr)
'''
TC : O(n log n)
SC : O(n)
'''