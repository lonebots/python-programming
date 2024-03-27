'''
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

 

Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Example 2:

Input: nums = [1,2,3], k = 0
Output: 0

 

Constraints:

    1 <= nums.length <= 3 * 104
    1 <= nums[i] <= 1000
    0 <= k <= 106

'''

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # brute force 
        # count = 0
        # for i in range(len(nums)) :
        #     for j in range(i, len(nums)) :
        #         prod  = 1
        #         for l in range(i,j+1) :
        #             prod *= nums[l]   
        #         if prod < k :
        #             count += 1
        # return count

        # two pointers sliding window
        if k <= 1 :
            return 0
        result = 0 
        right = left = 0
        prod = 1
        while right < len(nums) :
            prod *= nums[right] 
            while prod >= k :
                prod //= nums[left]
                left += 1
            
            result += right - left + 1
            right += 1
        
        return result