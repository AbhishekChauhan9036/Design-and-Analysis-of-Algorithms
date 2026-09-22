# https://www.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1
def job_sequencing(deadline,profit):
    jobs=[]
    for i in range(len(deadline)):
        jobs.append((profit[i],deadline[i]))

    jobs.sort(reverse=True)
    slots=[False]*(len(deadline)+1)
    count=0
    total_profit=0
    for profit,deadline in jobs:
        for time in range(deadline,0,-1):
            if slots[time]==False:
                slots[time]=True
                count+=1
                total_profit+=profit
                break
    return [count,total_profit]

deadline=[4,1,1,1]
profit=[20,10,40,30]
print(job_sequencing(deadline,profit))
'''
Time Complexity: O(n²)
Space Complexity: O(n)
'''

'''
Job Sequencing with Deadlines
1. Create a list of jobs using their profit and deadline.
2. Sort all jobs in decreasing order of profit.
3. Create time slots and mark all slots as empty.
4. For each job in sorted order:
      Start from its deadline and move backward to time slot 1.
      If an empty slot is found:
          Schedule the job in that slot.
          Increase the job count by 1.
          Add the job's profit to total profit.
          Break the loop.
5. Return the total number of scheduled jobs and maximum profit.
Job Sequencing - TC: O(N^2), SC: O(N)
'''