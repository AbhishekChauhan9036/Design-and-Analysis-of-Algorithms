def knapSack(weight, value, capacity, n):
    if capacity == 0 or n == 0:
        return 0

    if weight[n-1]>capacity:
        return knapSack(weight, value, capacity, n-1)

    include = value[n-1]+knapSack(weight, value, capacity-weight[n-1], n-1)
    exclude = knapSack(weight, value, capacity, n-1)
    return max(include, exclude)

weight = [18, 15, 10]
value = [25, 24, 15]
capacity = 20
print(knapSack(weight, value, capacity, len(weight)))
'''
TC - O(2)^n
SC - O(n)
'''


# https://www.geeksforgeeks.org/problems/assembly-line-scheduling/1