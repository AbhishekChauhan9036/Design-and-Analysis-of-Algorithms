def knapSack(weights, values, capacity):
    n = len(weights)
    ratio = []
    for i in range(n):
        ratio.append((values[i]/weights[i],weights[i],values[i]))  
    ratio.sort(reverse=True)
    total = 0
    for r, w, v in ratio:
        if capacity>=w:
            capacity = capacity - w
            total = total + v 
        else:
            total = total+r*capacity
            break
    return total
values = [25, 24, 15]
weights = [18, 15, 10]
capacity = 20
print(knapSack(weights, values, capacity))
'''
TC : O(n log n)
SC : O(n)
'''