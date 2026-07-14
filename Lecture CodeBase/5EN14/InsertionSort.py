arr = [3, 7, 19, 20, -4]
n = len(arr)
for i in range(1, n):
    key = arr[i]
    j = i-1
    while j>=0 and arr[j]>key:
        arr[j+1] = arr[j]
        j-=1

    arr[j+1] = key

print(arr)
"""
TC : O(n)^2
SC : O(1)
"""