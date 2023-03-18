'''
You have a 2-D grid of size m x n representing a box, and you have n balls. The box is open on the top and bottom sides.

Each cell in the box has a diagonal board spanning two corners of the cell that can redirect a ball to the right or to the left.

    A board that redirects the ball to the right spans the top-left corner to the bottom-right corner and is represented in the grid as 1.
    A board that redirects the ball to the left spans the top-right corner to the bottom-left corner and is represented in the grid as -1.

We drop one ball at the top of each column of the box. Each ball can get stuck in the box or fall out of the bottom. A ball gets stuck if it hits a "V" shaped pattern between two boards or if a board redirects the ball into either wall of the box.

Return an array answer of size n where answer[i] is the column that the ball falls out of at the bottom after dropping the ball from the ith column at the top, or -1 if the ball gets stuck in the box.

 

Example 1:

Input: grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
Output: [1,-1,-1,-1,-1]
Explanation: This example is shown in the photo.
Ball b0 is dropped at column 0 and falls out of the box at column 1.
Ball b1 is dropped at column 1 and will get stuck in the box between column 2 and 3 and row 1.
Ball b2 is dropped at column 2 and will get stuck on the box between column 2 and 3 and row 0.
Ball b3 is dropped at column 3 and will get stuck on the box between column 2 and 3 and row 0.
Ball b4 is dropped at column 4 and will get stuck on the box between column 2 and 3 and row 1.

Example 2:

Input: grid = [[-1]]
Output: [-1]
Explanation: The ball gets stuck against the left wall.

Example 3:

Input: grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
Output: [0,1,2,3,4,-1]

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 100
    grid[i][j] is 1 or -1.


'''

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        
        m, n = len(grid), len(grid[0])

        def dropBall(col) :
            for curr_row in range(m) :
                next_col = col + grid[curr_row][col]
                if next_col < 0 or next_col >= n or grid[curr_row][next_col] != grid[curr_row][col] :
                    return -1 
                col = next_col
            return col
        
        # drop ball through all the columns and append to result
        res = []
        for col in range(n) :
            res.append(dropBall(col))

        return res


# failed attempt
# class Solution:
#     def findBall(self, grid: List[List[int]]) -> List[int]:
#         m, n = len(grid), len(grid[0])

#         def dropBall (r,c,curr) :
#             if r == m - 1 :
#                 return c - 1 if curr == -1 else c + 1

#             if curr == -1 : # slide left case
#                 if c - 1 >= 0 and grid[r][c-1] == 1 :
#                     return -1
#                 elif r + 1 < m and c - 1 >= 0 :
#                     return dropBall(r+1,c-1,grid[r+1][c-1])
#                 else :
#                     return dropBall(r+1,c,grid[r+1][c])

#             elif curr == 1 : # slide right case
#                 if c + 1 < n and grid[r][c+1] == -1 :
#                     return -1
#                 if r + 1 < m and c + 1 < m :
#                     return dropBall(r+1,c+1,grid[r+1][c+1])
#                 else :
#                     return dropBall(r+1,c,grid[r+1][c])

#         res = []
#         # drop a ball through all the column and append the result
#         for c in range(n) :
#             column = dropBall(0,c,grid[0][c])
#             print(column) 
#             res.append(column if column  else -1)
        
#         return res

