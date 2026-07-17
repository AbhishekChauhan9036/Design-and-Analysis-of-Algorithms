def linearSerch(arr, target):
    n = len(arr)
    for i in range(0, n):
        if arr[i]==target:
            return i
    return -1

arr = [10,20,-4,90,2,22]
target = 67
ans = linearSerch(arr,target)
print(ans)