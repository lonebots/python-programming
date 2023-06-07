'''
Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.

 

Example 1:

Input: a = 2, b = 6, c = 5
Output: 3
Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c) 
'''

class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        flip_count = 0
        while a or b or c :
            if c & 1 :
                flip_count += 0 if (( a & 1 )or (b & 1)) else 1 
            else :
                flip_count += (a&1) + (b&1)
            a >>= 1 
            b >>= 1
            c >>= 1
        return flip_count