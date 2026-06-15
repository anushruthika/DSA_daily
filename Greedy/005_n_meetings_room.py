#  https://www.geeksforgeeks.org/problems/activity-selection-1587115620/1
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
