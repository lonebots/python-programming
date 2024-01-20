'''
Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

 

Example 1:

Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.

Example 2:

Input: arr = [11,81,94,43,3]
Output: 444

 

Constraints:

    1 <= arr.length <= 3 * 104
    1 <= arr[i] <= 3 * 104

'''

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        left = [-1] * n 
        right = [n] * n 

        stack = []

        for i, value in enumerate(arr) :
            while stack and arr[stack[-1]] >= value : 
                stack.pop()
            
            if stack : 
                left[i] = stack[-1]
            
            stack.append(i)
        
        stack = []

        for i in range(n-1, -1, -1) :
            while stack and arr[stack[-1]] > arr[i] :
                stack.pop()
            if stack : 
                right[i] =stack[-1]
            stack.append(i)

        mod = 10**9 + 7 

        result = sum((i - left[i]) * (right[i] - i) * value for i, value in enumerate(arr)) % mod
        
        return result