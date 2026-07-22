def linearSearch(arr, n, key):
    for i in range(n):
        if arr[i] == key:
            return i
    return -1

arr = [12, 78, -90, 23, 67, 54]
n = len(arr)
key = 5
ans = linearSearch(arr, n, key)
print(ans)
'''
TC : O(n)
SC : O(1)
'''