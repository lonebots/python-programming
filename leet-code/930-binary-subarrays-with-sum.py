'''
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.

 

Example 1:

Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]

Example 2:

Input: nums = [0,0,0,0,0], goal = 0
Output: 15

 

Constraints:

    1 <= nums.length <= 3 * 104
    nums[i] is either 0 or 1.
    0 <= goal <= nums.length

'''

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # one pass sliding window
        start = 0 
        prefix_zeros = 0
        current_sum = 0
        total_count = 0

        for end, num in enumerate(nums) :
            current_sum += num 

            while start < end and (nums[start] == 0 or current_sum > goal) :
                if nums[start] == 1 :
                    prefix_zeros = 0
                else :
                    prefix_zeros += 1 

                current_sum -= nums[start]
                start += 1
                
            # match goal 
            if current_sum == goal :
                total_count += 1 + prefix_zeros
        return total_count