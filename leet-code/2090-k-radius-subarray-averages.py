'''
You are given a 0-indexed array nums of n integers, and an integer k.

The k-radius average for a subarray of nums centered at some index i with the radius k is the average of all elements in nums between the indices i - k and i + k (inclusive). If there are less than k elements before or after the index i, then the k-radius average is -1.

Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.

The average of x elements is the sum of the x elements divided by x, using integer division. The integer division truncates toward zero, which means losing its fractional part.

For example, the average of four elements 2, 3, 1, and 5 is (2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75, which truncates to 2.
 

Example 1:


Input: nums = [7,4,3,9,1,8,5,2,6], k = 3
Output: [-1,-1,-1,5,4,4,-1,-1,-1]
Explanation:
- avg[0], avg[1], and avg[2] are -1 because there are less than k elements before each index.
- The sum of the subarray centered at index 3 with radius 3 is: 7 + 4 + 3 + 9 + 1 + 8 + 5 = 37.
  Using integer division, avg[3] = 37 / 7 = 5.
- For the subarray centered at index 4, avg[4] = (4 + 3 + 9 + 1 + 8 + 5 + 2) / 7 = 4.
- For the subarray centered at index 5, avg[5] = (3 + 9 + 1 + 8 + 5 + 2 + 6) / 7 = 4.
- avg[6], avg[7], and avg[8] are -1 because there are less than k elements after each index.
'''

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        # brute-force without prefix sum --> TLE
        # result = [] # store the resulting array
        # n = len(nums) 
        # for index in range(n) :
        #     if index + k >= n or index - k < 0 :
        #         result.append(-1)
        #     else :
        #         temp = sum(nums[index-k:index+k+1]) // (2*k + 1)
        #         result.append(temp)
        # return result

        # with prefix sum 
        n = len(nums)
        averages = [-1] * n
        prefix = [0] * (n+1) # at index = 0 the sum = 0

        for index in range(n) :
            prefix[index+1] = prefix[index] + nums[index]

        # edge case 1 : when k = 0 --> the radius range contain only 1 element thus return nums itself
        if k == 0 :
            return nums 

        # edge case 2 : when 2 * k + 1 > n then radius range is not possible so return average with all -1 
        if 2 * k + 1 > n : 
            return averages
        
        # case 3 : iterate over the range k to n - k and compute the averages 
        for index in range(k,n-k) :
            left, right = index - k, index + k 
            arraySum = prefix[right + 1] - prefix[left]
            averages[index] = arraySum // (2*k+1)

        return averages