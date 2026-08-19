def KnapSack(weights, values, capacity, n):
    if n == 0 or capacity == 0:
        return 0

    if weights[n-1] > capacity:
        return KnapSack(weights, values, capacity, n-1)

    include = values[n-1] + KnapSack(weights, values, capacity - weights[n-1], n-1)
    exclude = KnapSack(weights, values, capacity, n-1)
    return max(include, exclude)

values = [25, 24, 15]
weights = [18, 15, 10]
capacity = 25
print(KnapSack(weights, values, capacity, len(weights)))
'''
TC - O(2)^n
SC - O(n)
'''