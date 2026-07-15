arr = [6, 16, -45, -6, 4, 5]
n = len(arr)
for i in range(1, n):
    key = arr[i]
    j = i-1
    while arr[j]>key and j>=0:
        arr[j+1] = arr[j]
        j-=1
    arr[j+1] = key
print(arr)
"""
TC : O(n)^2
SC : O(1)
"""