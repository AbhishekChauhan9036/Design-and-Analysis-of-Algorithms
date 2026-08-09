def knapsack(weights, values, capacity, n):
    if n == 0 or capacity == 0:
        return 0

    # If item weight is greater than capacity
    if weights[n - 1] > capacity:
        return knapsack(weights, values, capacity, n - 1)

    # Two choices:
    # 1. Include the item
    # 2. Exclude the item
    include = values[n - 1] + knapsack(weights, values, capacity - weights[n - 1], n - 1)
    exclude = knapsack(weights, values, capacity, n - 1)
    return max(include, exclude)

# Example
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

n = len(weights)
print("Maximum Value:", knapsack(weights, values, capacity, n))

'''
Time: O(2^n)
Space: O(n) — recursion call stack
'''