arr = [6, 9, 3, 10, -13, -8, 90, 89, 43, 0]
n = len(arr)
gap = n//2
while gap>0:
    for i in range(gap, n):
        temp = arr[i]
        j = i
        while j>=gap and arr[j-gap]>temp:
            arr[j] = arr[j-gap]
            j-=gap
        arr[j] = temp
    gap//=2
print(arr)
'''
TC - 
    Average Case: O(n)^3/2
    Worst Case : O(n)
SC - O(1)
'''