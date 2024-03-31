'''
You are given an integer array nums and two integers minK and maxK.

A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

    The minimum value in the subarray is equal to minK.
    The maximum value in the subarray is equal to maxK.

Return the number of fixed-bound subarrays.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
Output: 2
Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].

Example 2:

Input: nums = [1,1,1,1], minK = 1, maxK = 1
Output: 10
Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.

 

Constraints:

    2 <= nums.length <= 105
    1 <= nums[i], minK, maxK <= 106
'''

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # approach 1 : brute force --> TLE
        # count_ = 0 
        # for i in range(len(nums)) :
        #     for j in range(i,len(nums)) :
        #         if nums[i] == minK and nums[j] == maxK :
        #             count_ += 1
        # return count_

        # approach 2 : 3 pointer 
        # res = 0
        # jmin = jmax = jbad = -1
        # for i,a in enumerate(nums):
        #     if not minK <= a <= maxK: jbad = i
        #     if a == minK: jmin = i
        #     if a == maxK: jmax = i
        #     res += max(0, min(jmin, jmax) - jbad)
        # return res

        # approach 3 : sliding window
        minFound = maxFound = False 
        minIdx = maxIdx = 0
        start = 0 
        result = 0
        for idx in range(len(nums)) :
            if nums[idx] < minK or nums[idx] > maxK :
                minFound = maxFound = False
                start = idx + 1
            
            if nums[idx] == minK :
                minFound = True
                minIdx = idx
                
            if nums[idx] == maxK :
                maxFound = True
                maxIdx = idx

            if minFound and maxFound :
                result += (min(minIdx,maxIdx) - start + 1) # + 1 since 0 indexing

        return result