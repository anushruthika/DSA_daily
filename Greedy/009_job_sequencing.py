# https://www.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1

# EDGE CASE
# | Job ID | Deadline | Profit |
# | ------ | -------- | ------ |
# | 1      | 4        | 20     |
# | 2      | 5        | 60     |
# | 3      | 6        | 70     |
# | 4      | 6        | 65     |
# | 5      | 4        | 25     |
# | 6      | 2        | 80     |
# | 7      | 2        | 10     |
# | 8      | 2        | 22     |


############################ BRUTE FORCE: Don't explain DFS approach
# TC: O(2^n)
# Each job has two choices:
# Take it / Don't take it

# SC: O(n + D)
# O(n) recursion stack
# O(D) slots array

class Solution:

    def jobSequencing(self, deadline, profit):

        n = len(deadline)

        max_jobs = 0
        max_profit = 0

        def dfs(i, slots, count, total):

            nonlocal max_jobs, max_profit

            if i == n:
                if total > max_profit:
                    max_profit = total
                    max_jobs = count
                return

            # Don't take current job
            dfs(i + 1, slots, count, total)

            # Try taking current job
            for t in range(deadline[i], 0, -1):

                if not slots[t]:

                    slots[t] = True

                    dfs(
                        i + 1,
                        slots,
                        count + 1,
                        total + profit[i]
                    )

                    slots[t] = False

                    break

        slots = [False] * (max(deadline) + 1)

        dfs(0, slots, 0, 0)

        return [max_jobs, max_profit]

############################ GREEDY NAIVE APPROACH
# TC: O(n log n + n * max_deadline)
# SC: # SC: O(max_deadline)

import heapq
class Solution:
    def jobSequencing(self, deadline, profit):
        jobs = []
        for i in range(len(profit)):
            jobs.append((profit[i],deadline[i]))
        jobs.sort(reverse= True)
        count =0
        tot = 0
        arr = [False]*max(deadline)
        for p,d in jobs:
            # print(p,d,arr,count,tot)
            while d-1>=0:
                if not arr[d-1]:
                    arr[d-1] = p
                    count+=1
                    tot+=p
                    break
                d -=1
        return [count,tot]


############################# DSU
# TC: O(n log n)
# - Sorting jobs takes O(n log n)
# - Each DSU find operation is nearly O(1) amortized (O(α(D)))
# - Total DSU work: O(n α(D))
# - Overall: O(n log n)

# SC: O(D)
# - Parent array of size (max_deadline + 1)
# - Ignoring the jobs array created by zip/sort

class Solution:

    class DisjointSet:

        def __init__(self, n):
            self.parent = [i for i in range(n + 1)]

        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def jobSequencing(self, deadline, profit):

        jobs = list(zip(profit, deadline))
        jobs.sort(reverse=True)

        max_deadline = max(deadline)
        ds = self.DisjointSet(max_deadline)

        count = 0
        total_profit = 0

        for p, d in jobs:

            slot = ds.find(d)

            if slot > 0:

                count += 1
                total_profit += p

                # mark slot occupied
                ds.parent[slot] = ds.find(slot - 1)

        return [count, total_profit]
            
                
