'''
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

 

Example 1:

Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).

Example 2:

Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1

Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2

 

Constraints:

    1 <= grid.length, grid[0].length <= 100
    0 <= grid[i][j] <=1
'''

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        q = []
        count = 0
        visited = set()
        m, n = len(grid), len(grid[0])

        def bfs(x,y) :
            nonlocal q, visited, m, n
            q.append((x,y)) 
            isClosed = True
            visited.add((x,y))

            while q :
                x,y = q.pop(0)
                for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)] :
                    xx, yy = x + dx, y + dy 
                    if xx < 0 or xx >= m or yy < 0 or yy >= n :
                        isClosed = False 
                    elif grid[xx][yy] == 0 and (xx,yy) not in visited :
                        visited.add((xx,yy))
                        q.append((xx,yy))
            return isClosed

        for r in range(m) :
            for c in range(n) :
                if grid[r][c] == 0 and (r,c) not in visited and bfs(r,c) :
                    count += 1

        
        # while q :
        #     isClosed = True
        #     while q :
        #         x, y = q.pop(0)
        #         if (x,y) in visited : 
        #             continue
        #         for dx, dy in  :
                    
        #             if (xx,yy) not in visited and 0 <= xx < m and 0 <= yy < n and grid[xx][yy] == 0 :
        #                 visited.add((xx,yy)) # mark it visited
        #                 q.append((xx,yy))
        #                 if xx == 0 or xx == m - 1 or yy == 0 or yy == n - 1 :
        #                     isClosed = False
                        
        #     if isClosed : 
        #         count += 1

        return count