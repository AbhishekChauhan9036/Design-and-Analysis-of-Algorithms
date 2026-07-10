arr = [12, 7, 9, -2, 67, 90]
for i in range(0,len(arr)-1):
    for j in range(i+1, len(arr)):
        if arr[i]>arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print(arr)
'''
Time Complexity: O(n)^2
Space Complexity: O(1)
'''