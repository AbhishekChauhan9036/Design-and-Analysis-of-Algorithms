def linearSearch(arr, n, key):
    for i in range(n):
        if arr[i] == key:
            return i
    return -1


arr = [3, 6, -3, 90, 23, 100, 98, 75]
key = -3
n = len(arr)
ans = linearSearch(arr, n, key)
if ans!=-1:
    print("Key Element is present in this array", ans)
else:
    print("Key Element is not present in this array")

'''
TC : O(n)
SC : O(1)
'''