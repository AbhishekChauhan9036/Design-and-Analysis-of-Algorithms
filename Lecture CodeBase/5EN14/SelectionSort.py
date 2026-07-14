arr = [3, 7, 19, 20, -4]
n = len(arr)
for i in range(n-1):
    min = i
    for j in range(i+1, n):
        if arr[j]< arr[min]:
            min = j
    arr[i], arr[min] = arr[min], arr[i]
print(arr)
"""
TC : O(n)^2
SC : O(1)
"""