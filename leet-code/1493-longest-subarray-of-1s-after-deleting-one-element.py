'''
Given a binary array nums, you should delete one element from it.
Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
'''
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_window = 0 # stores the final answer
        zero_count = 0

        # edge case 1 
        # when all the elements are 1 we are forced to delete one 1 from the list
    

        # we need a start and end ; start = 0 and end < len(nums)
        # start changes if numbe of 0's > 1 
        # end shift always to the right
        start = 0 
        for i in range(len(nums)) :
            if nums[i] == 0 :
                zero_count += 1 
            
            while zero_count > 1 :
                if nums[start] == 0 :
                    zero_count -= 1 
                start += 1 

            max_window = max(max_window,i-start)
        
        return max_window