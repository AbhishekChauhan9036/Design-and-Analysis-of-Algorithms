def binarySerch(arr, key, n):
    low = 0
    high = n-1
    while low<=high:
        mid = (low + high)//2
        if arr[mid] == key:
            return mid
        elif arr[mid]<key:
            low = mid + 1
        else:
            high = mid -1
    return -1

arr = [2, 4, 9, 15, 20, 30]
key = 15
n = len(arr)
ans = binarySerch(arr, key, n)
print(ans)
'''
TC : O(log n)
SC : O(1)
'''