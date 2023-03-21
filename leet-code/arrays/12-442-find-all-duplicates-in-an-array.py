"""
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

Example 2:

Input: nums = [1,1,2]
Output: [1]

Example 3:

Input: nums = [1]
Output: []

 

Constraints:

    n == nums.length
    1 <= n <= 105
    1 <= nums[i] <= n
    Each element in nums appears once or twice.

"""


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        The trick is :
            1. All the value in nums can refer to an index = n -1 (which is valid)
            2. First time when we seen a value n make the value at index (n -1) as negative
            3. again when we see that value check if the value at that index is negative or not , if negative then add the (index + 1) to resutl array

        """

        res = []

        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                res.append(index + 1)
            nums[index] = -nums[index]

        return res
