'''
You are given a rows x cols matrix grid representing a field of cherries where grid[i][j] represents the number of cherries that you can collect from the (i, j) cell.

You have two robots that can collect cherries for you:

    Robot #1 is located at the top-left corner (0, 0), and
    Robot #2 is located at the top-right corner (0, cols - 1).

Return the maximum number of cherries collection using both robots by following the rules below:

    From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
    When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.
    When both robots stay in the same cell, only one takes the cherries.
    Both robots cannot move outside of the grid at any moment.
    Both robots should reach the bottom row in grid.

 

Example 1:

Input: grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
Output: 24
Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
Cherries taken by Robot #1, (3 + 2 + 5 + 2) = 12.
Cherries taken by Robot #2, (1 + 5 + 5 + 1) = 12.
Total of cherries: 12 + 12 = 24.

Example 2:

Input: grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
Output: 28
Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
Cherries taken by Robot #1, (1 + 9 + 5 + 2) = 17.
Cherries taken by Robot #2, (1 + 3 + 4 + 3) = 11.
Total of cherries: 17 + 11 = 28.

 

Constraints:

    rows == grid.length
    cols == grid[i].length
    2 <= rows, cols <= 70
    0 <= grid[i][j] <= 100

'''

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        # Create 3D DP table with initial values of 0
        dp = [[[0] * m for _ in range(m)] for _ in range(n)]

        # Set the starting point value (top-left and top-right corner)
        cherries = 0
        dp[0][0][m - 1] = grid[0][0] + grid[0][m - 1]

        # Iterate through each row from second onwards
        for i in range(1, n):
            # Iterate through each column for robot 1
            for j in range(m):
                # Iterate through each column for robot 2
                for k in range(m):
                    # Skip invalid states:
                    # - Both robots in the same row (j > i)
                    # - Robot 2 left of robot 1 (k < m - i - 1)
                    # - Robot 1 further right than robot 2 (j > k)
                    if j > i or k < m - i - 1 or j > k:
                        continue
                    # Base case: no moves possible, use previous state
                    dp[i][j][k] = dp[i - 1][j][k]
                    # Explore moves for robot 1:
                    # - Up-diagonal with robot 2 at same position
                    if j - 1 >= 0:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - 1][k])
                    # - Up-diagonal with robot 2 one step left/right
                    if j - 1 >= 0 and k - 1 >= 0:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - 1][k - 1])
                    if j - 1 >= 0 and k + 1 < m:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - 1][k + 1])
                    # Explore moves for robot 2:
                    # - Up-diagonal with robot 1 at same position
                    if j + 1 < m:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j + 1][k])
                    # - Up-diagonal with robot 1 one step left/right
                    if j + 1 < m and k - 1 >= 0:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j + 1][k - 1])
                    if j + 1 < m and k + 1 < m:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j + 1][k + 1])
                    # Explore horizontal moves for both robots:
                    # - Both robots move left
                    if k - 1 >= 0:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k - 1])
                    # - Both robots move right
                    if k + 1 < m:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k + 1])
                    # Add cherries only if robots are in different positions
                    if j != k:
                        dp[i][j][k] += grid[i][j] + grid[i][k]
                    else:
                        dp[i][j][k] += grid[i][j]  # Only one robot picks if they land in the same cell
                    # Update maximum cherries collected so far
                    cherries = max(cherries, dp[i][j][k])

        return cherries
