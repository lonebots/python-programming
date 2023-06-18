'''
You are given an m x n integer matrix grid, where you can move from a cell to any adjacent cell in all 4 directions.

Return the number of strictly increasing paths in the grid such that you can start from any cell and end at any cell. Since the answer may be very large, return it modulo 109 + 7.

Two paths are considered different if they do not have exactly the same sequence of visited cells.

 

Example 1:


Input: grid = [[1,1],[3,4]]
Output: 8
Explanation: The strictly increasing paths are:
- Paths with length 1: [1], [1], [3], [4].
- Paths with length 2: [1 -> 3], [1 -> 4], [3 -> 4].
- Paths with length 3: [1 -> 3 -> 4].
The total number of paths is 4 + 3 + 1 = 8.
Example 2:

Input: grid = [[1],[2]]
Output: 3
Explanation: The strictly increasing paths are:
- Paths with length 1: [1], [2].
- Paths with length 2: [1 -> 2].
The total number of paths is 2 + 1 = 3.
'''

'''
approach 1 : 
sort the list of number and using dp to compute the over all count of strictly increasing paths 

approach 2 : 
using dp and dfs 
'''


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int: 
        m, n = len(grid), len(grid[0])
        mod = 10 ** 9 + 7
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        dp = [[0] * n for _ in range(m)]
        
        def dfs(i, j):
            # If dp[i][j] is non-zero, it means we have got the value of dfs(i, j),
            # so just return dp[i][j].
            if dp[i][j]:
                return dp[i][j]

            # Otherwise, set answer = 1, the path made of grid[i][j] itself.
            answer = 1

            # Check its four neighbor cells, if a neighbor cell grid[prevI][prevJ] has a
            # smaller value, we move to this cell and solve the subproblem: dfs(prevI, prevJ).
            for di, dj in directions:
                prev_i, prev_j = i + di, j + dj
                if 0 <= prev_i < m and 0 <= prev_j < n and grid[prev_i][prev_j] < grid[i][j]:
                    answer += dfs(prev_i, prev_j) % mod
            
            # Update dp[i][j], so that we don't recalculate its value later.
            dp[i][j] = answer
            return answer
        
        # Iterate over all cells grid[i][j] and sum over dfs(i, j).
        return sum(dfs(i, j) for i in range(m) for j in range(n)) % mod