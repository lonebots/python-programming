'''
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

 

Example 1:

Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.

Example 2:

Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 500
    grid[i][j] is either 0 or 1.

'''

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # dfs solution 
        def dfs (x,y) :
            nonlocal grid
            grid[x][y] = 0 
            for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)] :
                xx, yy = x + dx, y + dy
                if 0 <= xx < m and 0 <= yy < n and grid[xx][yy] :
                    dfs(xx,yy)

        m, n = len(grid), len(grid[0])
        for r in range(m) :
            for c in range(n) :
                # take all boundary 1's and do dfs from that r,c
                if grid[r][c] == 1 and  (r == 0 or c == 0 or r == m - 1 or c == n - 1) : 
                    dfs(r,c)

        res = 0
        for r in range(m) :
            for c in range(n) :
                res += grid[r][c]
        return res
        
# failed attempt 

# class Solution:
#     def numEnclaves(self, grid: List[List[int]]) -> int:
#         q, visited, m, n = [], set(), len(grid), len(grid[0])
#         res = 0

#         def bfs (i,j) :
#             nonlocal grid, m, n, q, visited
#             count = 0
#             q.append((i,j))
#             isClosed = True
#             while q :
#                 x, y = q.pop(0)
#                 for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)] :
#                     xx, yy = x + dx, y + dy 
#                     if xx < 0 or yy < 0 or xx >= m or yy >= n :
#                         isClosed = False
                        
#                     elif (xx,yy) not in visited and grid[xx][yy] == 1 :
#                         visited.add((xx,yy))
#                         count += 1
#                         q.append((xx,yy))
 
#             return count if isClosed else 0

#         # find all possible island start points
#         for r in range(m) :
#             for c in range(n) :
#                 if grid[r][c] == 1 and (r,c) not in visited:
#                     res += bfs(r,c)

#         return res