"""
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

 

Example 1:

Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.

Example 2:

Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8

"""
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        diag_sum = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])) :
                if i == j or i + j == len(mat) - 1 :
                    diag_sum += mat[i][j]

        return diag_sum

