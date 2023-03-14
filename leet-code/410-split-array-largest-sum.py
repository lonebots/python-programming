'''
Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array.

 

Example 1:

Input: nums = [7,2,5,10,8], k = 2
Output: 18
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.

Example 2:

Input: nums = [1,2,3,4,5], k = 2
Output: 9
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.

'''

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # helper function 
        def canSplit(largest) :
            subarray = 0
            currSum = 0
            for n in nums :
                currSum += n 
                if currSum > largest : 
                    currSum = n
                    subarray += 1 
            return subarray + 1 <= k

        l, r = max(nums),sum(nums)
        res = sum(nums)
        while l <= r :
            mid = l + (r - l) // 2 
            if canSplit(mid) :
                res = mid
                r = mid - 1
            else :
                l = mid + 1

        return res
