def knapsack(weight, value, capacity):
    n = len(weight)
    # Calculate value/weight ratio
    ratio = []
    for i in range(n):
        ratio.append((value[i] / weight[i], weight[i], value[i]))
    # Sort by ratio in descending order
    ratio.sort(reverse=True)
    total = 0
    for r, w, v in ratio:
        if capacity >= w:
            capacity = capacity - w
            total = total + v
        else:
            total = total + r * capacity
            break
    return total

weight = [10, 20, 30]
value = [60, 100, 120]
capacity = 50
print(knapsack(weight, value, capacity))

'''
Time Complexity: O(n log n)
Space Complexity: O(n)
'''

'''
1. Calculate Value / Weight
2. Sort items by highest ratio
3. Take the highest ratio item first
4. If the complete item cannot fit, take its fraction
5. Stop when the bag is full
'''