'''
An array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

You must solve it in O(log(arr.length)) time complexity.

 

Example 1:

Input: arr = [0,1,0]
Output: 1
Example 2:

Input: arr = [0,2,1,0]
Output: 1
Example 3:

Input: arr = [0,10,5,2]
Output: 1
'''

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # binary search 
        left = 0 
        right = len(arr)-1 

        while left < right :
            # find mid
            mid = (left + right) // 2 

            # conditions 
            if  mid == 0 or mid == len(arr) - 1  or  arr[mid-1] < arr[mid] > arr[mid+1] :
                return mid 
            
            elif arr[mid-1] < arr[mid] < arr[mid+1] :
                left = mid 
            
            else : 
                right = mid 