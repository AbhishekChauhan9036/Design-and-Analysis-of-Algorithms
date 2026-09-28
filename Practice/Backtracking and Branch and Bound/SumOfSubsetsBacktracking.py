'''
Step 1: Start with a set of numbers and a target sum.
Step 2: Start from the first element.
Step 3: Choose the current element and add it to the subset.
Step 4: Check whether the current sum equals the target sum.
Step 5: If equal, print the subset.
Step 6: If the sum exceeds the target, backtrack.
Step 7: If not, move to the next element and continue.
Step 8: Remove the selected element and try the next possibility.

Time Complexity: O(2^N)
Space Complexity: O(N) recursion stack.
'''
N=4
arr=[10,7,5,18]
target=25
subset=[]
def sum_subset(i,total):
    if total==target:
        print(subset)
        return
    if i==N or total>target:
        return
    subset.append(arr[i])
    sum_subset(i+1,total+arr[i])
    subset.pop()
    sum_subset(i+1,total)
sum_subset(0,0)