'''
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

Example 1:

Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:

Input: n = 1
Output: [[1]]

'''


class Solution:
    def generateMatrix(self, n):
        matrix = [[0] * n for _ in range(n)]
        x, y, dx, dy = 0, 0, 1, 0
        for i in range(n*n):
            matrix[y][x] = i + 1
            if not 0 <= x + dx < n or not 0 <= y + dy < n or matrix[y+dy][x+dx] != 0:
                dx, dy = -dy, dx
            x, y = x + dx, y + dy
        return matrix