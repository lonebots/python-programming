'''
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:

Input: nums = [1], k = 1
Output: [1]

 

Constraints:

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
    1 <= k <= nums.length


'''


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # brute force : TLE
        # result = []

        # for i in range(len(nums)-k+1) :
        #     result.append(max(nums[i:i+k]))

        # return result

        # approach 2 : avoid repeated word 
        # monotonically decreasing queue
        q = []
        result = []
        l = r = 0 
        while r < len(nums) :
            # remove smaller element at end of queue
            while q and nums[q[-1]] < nums[r]  :
                q.pop()

            q.append(r) # add r 

            # remove elements from the left of the queue
            if l > q[0] :
                q.pop(0)

            # add to result if window size is met
            if r + 1 >= k :
                result.append(nums[q[0]])
                l += 1
            
            r += 1
            

        return result

