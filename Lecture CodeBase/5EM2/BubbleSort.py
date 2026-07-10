arr = [12, -14, 6, 7, 2]
for i in range(0,len(arr)+1):
    for j in range(0,len(arr)-i-1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
print(arr)

'''
Time Complexity: O(n)^2
Space Complexity: O(1)
'''