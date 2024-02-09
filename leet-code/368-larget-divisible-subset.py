'''
Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

    answer[i] % answer[j] == 0, or
    answer[j] % answer[i] == 0

If there are multiple solutions, return any of them.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.

Example 2:

Input: nums = [1,2,4,8]
Output: [1,2,4,8]

 

Constraints:

    1 <= nums.length <= 1000
    1 <= nums[i] <= 2 * 109
    All the integers in nums are unique.
'''

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)

        groupSize = [1] * n
        prevElement = [-1] * n 
        maxIndex = 0

        for i in range(n) :
            for j in range(i) : 
                if nums[i] %  nums[j] == 0 :
                    if groupSize[i] < 1 + groupSize[j] :
                        groupSize[i] = 1 + groupSize[j]
                        prevElement[i] = j 
            if groupSize[i] > groupSize[maxIndex] :
                maxIndex = i 

        result = []

        while maxIndex != -1 :
            result.insert(0,nums[maxIndex])
            maxIndex = prevElement[maxIndex]
        
        return result