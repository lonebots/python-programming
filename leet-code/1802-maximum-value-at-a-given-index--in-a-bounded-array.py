''' 
You are given three positive integers: n, index, and maxSum. You want to construct an array nums (0-indexed) that satisfies the following conditions:

    nums.length == n
    nums[i] is a positive integer where 0 <= i < n.
    abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
    The sum of all the elements of nums does not exceed maxSum.
    nums[index] is maximized.

Return nums[index] of the constructed array.

Note that abs(x) equals x if x >= 0, and -x otherwise.

 

Example 1:

Input: n = 4, index = 2,  maxSum = 6
Output: 2
Explanation: nums = [1,2,2,1] is one array that satisfies all the conditions.
There are no arrays that satisfy all the conditions and have nums[2] == 3, so 2 is the maximum nums[2].

'''

class Solution(object):
    def getSum(self, index, value, n) :
        """
        :type index: int
        :type value: int
        :type n: int
        """
        count = 0
        
        # on left side of index : 
        # if value > index, there are index + 1 number in Arithmetic sequence
        # [ value - index , ... , value - 1, value] 
        # otherwise there are value number in arithmetics sequence.
        # [1, 2, 3, ..., value - 1, value], plus sequence of length ( index - value + 1) of 1s.
        if value > index : 
            count += ( value + value - index) * ( index + 1 ) // 2
        else :
            count += ( value + 1) * value // 2 + (index - value + 1)

        # on the right side of index :
        # if value >= n - index , there are n - index numbers in the Arithmetic sequence 
        # [value, value - 1, ..., value - n + 1 + index] ,
        # otherwise, there are value numbers in the arithmetic sequence;
        # [value, value - 1, ..., 1] , plus a sequence of lenght ( n - index - value ) of 1s.
        if value >= n - index :
            count += (value + value - n + 1 + index ) * (n - index) //2 
        else :
            count += ( value + 1) * value//2 + ( n - index - value)
    
        return count - value

    def maxValue(self, n, index, maxSum):
        """
        :type n: int
        :type index: int
        :type maxSum: int
        :rtype: int
        """ 
        left, right = 1, maxSum
        while left < right :
            mid = ( left + right + 1) // 2 
            if self.getSum(index, mid, n) <= maxSum :
                left = mid
            else :
                right = mid - 1
        return left