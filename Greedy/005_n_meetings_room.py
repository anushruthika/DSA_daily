#  https://www.geeksforgeeks.org/problems/activity-selection-1587115620/1

########## BRUTE FORCE
# TC: O(2^n)
# Every meeting has:
#   Take
#   Don't Take

# SC: O(n)
# Recursion stack
class Solution:

    def maxMeetings(self, start, end):

        meetings = list(zip(start, end))
        meetings.sort()

        def dfs(i, last_end):

            if i == len(meetings):
                return 0

            # Skip current meeting
            not_take = dfs(i + 1, last_end)

            take = 0

            if meetings[i][0] > last_end:
                take = 1 + dfs(i + 1, meetings[i][1])

            return max(take, not_take)

        return dfs(0, -1)

####################### GREEDY OPTIMAL
# TC: O(n log n)
# Sorting meetings: O(n log n)
# Single traversal: O(n)

# SC: O(n)
# meetings list

class Solution:
    def activitySelection(self, start, finish):
        #code here
        meetings = list(zip(finish, start))
        meetings.sort()
        count = 0
        last_selected_finish = None
        for i in range(len(meetings)):
            if last_selected_finish == None:
                last_selected_finish = meetings[i][0]
                count+=1
            elif meetings[i][1]>last_selected_finish:
                count+=1
                last_selected_finish = meetings[i][0]
        return count
