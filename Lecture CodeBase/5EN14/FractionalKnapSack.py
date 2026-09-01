def fKnapsack(profit, weight, capacity):
    n = len(weight)
    ratio = []
    for i in range(n):
        ratio.append((profit[i]/weight[i],weight[i],profit[i]))
    ratio.sort(reverse=True)
    # print(ratio)
    total = 0
    for r, w, v in ratio:
        if capacity>=w:
            capacity = capacity-w
            total = total+v 
        else:
            total = total+r*capacity
            break
    return total

profit = [25, 24, 15]
weight = [18, 15, 10]
capacity = 20
print(fKnapsack(profit, weight, capacity))
'''
TC : O(n log n)
SC : O(n)
'''