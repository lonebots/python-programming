'''
You are given an array of events where events[i] = [startDayi, endDayi, valuei]. The ith event starts at startDayi and ends at endDayi, and if you attend this event, you will receive a value of valuei. You are also given an integer k which represents the maximum number of events you can attend.

You can only attend one event at a time. If you choose to attend an event, you must attend the entire event. Note that the end day is inclusive: that is, you cannot attend two events where one of them starts and the other ends on the same day.

Return the maximum sum of values that you can receive by attending events.

 

Example 1:



Input: events = [[1,2,4],[3,4,3],[2,3,1]], k = 2
Output: 7
Explanation: Choose the green events, 0 and 1 (0-indexed) for a total value of 4 + 3 = 7.
'''

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # we can attend event when end_day[i] != start_day[j] ==> we should sort
        events.sort()

        # create a dp
        n = len(events)
        dp = [[-1] * n for _ in range(k+1)]

        # take a note of all the start times 
        starts = [start for start,end,value in events]


        # dfs 
        def dfs(curr_index,count):
            if count == 0 or curr_index == n :
                return 0
            
            if dp[count][curr_index] != -1 : # already calculated
                return dp[count][curr_index]

            # find the nearest available event after attending event 0
            next_index = bisect_right(starts,events[curr_index][1])

            dp[count][curr_index] = max(dfs(curr_index+1,count), events[curr_index][2] + dfs(next_index,count-1))
            return dp[count][curr_index]

        return dfs(0,k)

# notes on bisect

# bisect_left returns the largest index to insert the element with respect to <
# bisect_right returns the largest index to insert the element with respect to <=
# For instance, if your data is [0, 0, 0] and you query for 0:

# bisect_left returns index 0, because that's the largest possible insert index where the inserted element is truly smaller.
# bisect_right returns index 3, because with "smaller or equal" the search advances through identical elements.
# This behavior can be simplified to:

# bisect_left would insert elements to the left of identical elements.
# bisect_right would insert elements to the right of identical elements.