arr = [12, 2, 45, 65, -9, 4, 5, 8, 67, 90]
n = len(arr)
gap = n//2
while gap>0:
    for i in range(gap, n):
        temp = arr[i]
        j = i
        while j>= gap and arr[j-gap] > temp:
            arr[j] = arr[j-gap]
            j -= gap
        
            arr[j] = temp
    gap//=2
print(arr)
"""
TC - 
    Average Case: O(n)^1.5
    Worst Case : O(n)^2

SC : O(1)
"""