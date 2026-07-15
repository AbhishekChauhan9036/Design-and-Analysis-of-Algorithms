arr = [5, 9, -2, 3, 6]
n = len(arr)
for i in range(n-1):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp

print(arr)
"""
TC : O(n)^2
SC : O(1)
"""