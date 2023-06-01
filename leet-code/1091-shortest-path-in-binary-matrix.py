''' 
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

    All the visited cells of the path are 0.
    All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).

The length of a clear path is the number of visited cells of this path.

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 2

'''
# solved using a normal binary search 
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # edge case : no path
        if grid[0][0] != 0 :
            return -1 

        n = len(grid[0])    
        # bfs 
        q = [[0,0,1]] # (x,y,path)
        visited = set()
        while q :
            [x,y,path] = q.pop(0)
            if x == n -1 and y == n - 1 :
                return path
            
            for [nx,ny] in [[x-1,y],[x+1,y],[x,y+1],[x,y-1], [x-1,y-1], [x+1,y+1], [x-1,y+1],[x+1,y-1]] :
                if (nx,ny) not in visited and (0 <= nx < n) and (0 <= ny < n) and grid[nx][ny] == 0 :
                    visited.add((nx,ny))
                    q.append([nx,ny, path + 1])

        return -1  # no path