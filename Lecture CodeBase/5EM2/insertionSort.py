arr = [12, 9, 34, -3, 7]
for i in range(1,len(arr)):
    key = arr[i]
    j = i-1
    while j>=0 and arr[j]>key:
        arr[j+1] = arr[j]
        j=j-1
    arr[j+1] = key
print(arr)
'''
Time Complexity: O(n)^2
Space Complexity: O(1)
'''