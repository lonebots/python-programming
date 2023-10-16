'''
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:

Input: rowIndex = 0
Output: [1]

Example 3:

Input: rowIndex = 1
Output: [1,1]

'''

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        prev = 1 
        for k in range(1,rowIndex + 1) :
            next_val = prev * (rowIndex - k +1) // k 
            res.append(next_val)
            prev = next_val
        return res