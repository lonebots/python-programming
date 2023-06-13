'''
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

 

Example 1:

Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
'''

class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0 
        n = len(grid)
        for i in range(n) :
            for j in range(n) :
                match = True # checks if row and col matches or not?
                for k in range(n) :
                    if grid[i][k] != grid[k][j] :
                        match = False 
                        break 
                count += int(match) # increment count if a match occurs
        return count