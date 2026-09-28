'''
Step 1: Start with items having weights, values, and a capacity.
Step 2: Start from the first item.
Step 3: Include the current item if it fits in the knapsack.
Step 4: Calculate the current weight and value.
Step 5: Move to the next item.
Step 6: Also try the case of excluding the current item.
Step 7: Compare both choices and keep the maximum value.
Step 8: Continue until all items are checked.

Time Complexity: O(2^N)
Space Complexity: O(N) recursion stack.
'''
N=4
weights=[2,3,4,5]
values=[3,4,5,6]
capacity=5
def knapsack(i,weight,value):
    if i==N or weight==capacity:
        return value
    if weight+weights[i]<=capacity:
        include=knapsack(i+1,weight+weights[i],value+values[i])
    else:
        include=0
    exclude=knapsack(i+1,weight,value)
    return max(include,exclude)
print("Maximum Value:",knapsack(0,0,0))