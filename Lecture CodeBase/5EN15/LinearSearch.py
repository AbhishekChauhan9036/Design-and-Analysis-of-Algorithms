def linearSearch(arr, n, key):
    for i in range(n):
        if arr[i]==key:
            return i
    return -1

arr = [15, 14, 13, -6, 4, 20]
key = 5
n = len(arr)
ans = linearSearch(arr, n, key)
print(ans)
'''
TC : O(n)
SC : O(1)
'''