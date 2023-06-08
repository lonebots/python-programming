''' 
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

 

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.

'''

class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # negCount = 0
        # for i in range(len(grid)) :
        #     for j in range(len(grid[0])) :
        #         if grid[i][j] < 0 :
        #             negCount += 1 
        # return negCount


        negCount = 0 
        for row in grid :
            left, right = 0 , len(grid[0]) -1
            while left <= right :
                mid = ( right + left ) //2
                if row[mid] < 0 :
                    right = mid - 1
                else :
                    left = mid + 1
            negCount += (len(grid[0]) - left)
        return negCount