'''
You are given an integer array nums and a positive integer k.

Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

A subarray is a contiguous sequence of elements within an array.

 

Example 1:

Input: nums = [1,3,2,3,3], k = 2
Output: 6
Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].

Example 2:

Input: nums = [1,4,2,1], k = 3
Output: 0
Explanation: No subarray contains the element 4 at least 3 times.

'''

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_element = max(nums)
        count_max_elements = 0
        start = 0 
        result = 0

        for end in range(len(nums)) :
            if nums[end] == max_element : 
                count_max_elements += 1 

            while count_max_elements == k : 
                if nums[start] == max_element : 
                    count_max_elements -= 1 
                start +=1 

            result += start 
                
        return result