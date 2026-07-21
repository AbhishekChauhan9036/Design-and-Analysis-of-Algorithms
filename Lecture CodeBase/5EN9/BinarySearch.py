def binarySerch(arr, n, key):
    low = 0
    high = n-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid] == key:
            return mid
        elif arr[mid]<key:
            low = mid+1
        else:
            high = mid -1
    return -1

arr = [2, 3, 4, 7, 9, 12, 15]
key = 5
n = len(arr)
ans = binarySerch(arr, n, key)
print(ans)
'''
TC : O(log n)
SC : O(1)
'''