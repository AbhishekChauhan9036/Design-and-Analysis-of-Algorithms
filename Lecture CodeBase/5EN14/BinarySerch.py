def binarySerch(arr, key):
    low = 0
    high = len(arr)-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid] == key:
            return mid
        elif arr[mid]<key:
            low = mid+1
        else:
            high = mid -1
    return -1

arr = [2, 4, 9, 15, 17, 19, 21]
key = 18
ans = binarySerch(arr, key)
print(ans)
'''
TC - O(log n)
SC - O(1)
'''