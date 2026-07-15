arr = [6, 16, 45, -6, 4, 5]
n = len(arr)
for i in range(n-1):
    min = i
    for j in range(i+1, n):
        if(arr[j] < arr[min]):
            min = j
        
    if(min != i):
        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp
print(arr)
"""
TC : O(n)^2
SC : O(1)
"""