
# Q6. Network Dispatcher — Thermal Throttling Makespan

# You are simulating a network dispatcher that routes an array of N tasks, given by their base processing times, to M identical servers (numbered 1 to M).

# The dispatcher assigns tasks one by one according to the following strict system protocols:

# 1. Priority Queueing:
# The dispatcher always selects the largest remaining unassigned task in the network. If multiple tasks have the exact same base processing time, it selects the one that appeared earliest in the original input sequence.

# 2. Load Balancing:
# The selected task is immediately assigned to the server with the lowest current total load. If multiple servers are tied for the lowest load, the task is routed to the server with the smallest ID.

# 3. Thermal Throttling (Fatigue):
# Because servers heat up, tasks take longer the more a server is used.

# The actual processing time added to a server's load is calculated as:

#     p + (k * w)

# Where:
# - p is the task's base processing time.
# - k is the number of tasks already assigned to this specific server prior to this task.
# - w is a constant thermal penalty parameter.

# Return the makespan, which is the maximum total load across all M servers after all N tasks have been dispatched.

# Find the maximum total load on a single server.


# SAMPLE TEST CASE

# Input:
# tasks = [6, 5, 4, 3, 2]
# M = 2
# w = 2

# Explanation:

# Tasks are selected in descending order: 6, 5, 4, 3, 2.

# Step 1:
# Task = 6
# Selected server = S1
# k = 0
# Actual time = 6 + (0 * 2) = 6
# Server loads = [6, 0]

# Step 2:
# Task = 5
# Selected server = S2
# k = 0
# Actual time = 5 + (0 * 2) = 5
# Server loads = [6, 5]

# Step 3:
# Task = 4
# Selected server = S2
# k = 1
# Actual time = 4 + (1 * 2) = 6
# Server loads = [6, 11]

# Step 4:
# Task = 3
# Selected server = S1
# k = 1
# Actual time = 3 + (1 * 2) = 5
# Server loads = [11, 11]

# Step 5:
# Task = 2
# Both servers have equal load (11).
# Therefore, select S1 because it has the smaller server ID.

# k = 2
# Actual time = 2 + (2 * 2) = 6
# Server loads = [17, 11]

# Output:
# 17

# Explanation:
# The final server loads are [17, 11].
# The makespan is the maximum load across all servers.

# Therefore, the answer is 17.

# ###########################################################################################################################################
import heapq
def solve(tasks, M, w):
    tasks = sorted([(v,i) for i,v in enumerate(tasks)],reverse = True)
    pq = []
    d = {}
    for server in range(M):
        d[server] = 0
        heapq.heappush(pq,(0,server,-1,0))
    max_cost = 0
    for v,i in tasks:
        pt,ser,ind,batch = heapq.heappop(pq)
        
        cost = v+batch*w
        # print(pt,ind,ser,batch,cost)
        d[ser]+=cost
        max_cost = max(max_cost,d[ser])
        heapq.heappush(pq,(cost+pt,ser,i,batch+1))
    #     print(pq)
    # print(d)
    return max_cost


test_cases = [
    # (tasks, M, w, expected_output)

    ([6, 5, 4, 3, 2], 2, 2, 17),
    ([3, 1, 2], 1, 1, 9),
    ([9, 8], 3, 5, 9),
    ([8, 7, 6, 5], 2, 3, 16),
    ([8, 7, 6, 5, 4], 2, 0, 17),
    ([4, 2], 4, 10, 4),
    ([10, 1, 1, 1, 1], 2, 2, 16),
    ([2, 2, 2, 2, 2], 2, 1, 9),
]

for i, (tasks, M, w, expected) in enumerate(test_cases, 1):
    actual = solve(tasks, M, w)

    status = "PASS" if actual == expected else "FAIL"

    print(f"Test Case {i}: {status}")
    print(f"  Input: tasks={tasks}, M={M}, w={w}")
    print(f"  Expected: {expected}")
    print(f"  Actual:   {actual}")
    print()
