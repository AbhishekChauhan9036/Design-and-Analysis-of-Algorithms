# https://www.geeksforgeeks.org/problems/activity-selection-1587115620/1

class Solution:
    def activitySelection(self, start: list[int], finish: list[int]) -> int:
        activities = []

        for i in range(len(start)):
            activities.append((start[i], finish[i]))

        # Sort by finish time
        activities.sort(key=lambda x: x[1])

        count = 0
        last_finish = -1

        for start_time, finish_time in activities:
            if start_time > last_finish:
                count += 1
                last_finish = finish_time

        return count
        
'''
Very simple logic
First, sort activities according to finish time.
Select the activity that finishes earliest.
Then select the next activity whose start time > previous finish time.
Continue until all activities are checked.
'''
        
'''
Time Complexity: O(n log n)
Space Complexity: O(n)
'''
        