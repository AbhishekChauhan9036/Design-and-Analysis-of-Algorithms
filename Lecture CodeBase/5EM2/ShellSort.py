arr = [19, 7, 6, 5, 48, -9, 2, 3, 24, 25]
n = len(arr)
gap = n//2
while gap>0:
    for i in range(gap, n):
        temp = arr[i]
        j = i
        while j>= gap and arr[j-gap]>temp:
            arr[j] = arr[j-gap]
            j = j-gap
        arr[j] = temp
    gap//=2
print(arr)
'''
TC -Average Case: O(n)^3/2
    Worst Case: O(n)^2
SC : O(1)
'''