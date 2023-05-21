'''
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.

 

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1

Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2

Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1

'''
class Solution(object):
    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        # start with dfs change all island A land to 2 , now we have 
        # 0 -> water 
        # 1 -> island B
        # 2 -> island A 
        # do bfs and find the shortest path between islands A and B.

        n = len(grid)
        # find the first cell of island A 
        first_x, first_y = -1, -1 
        for i in range(n) :
            for j in range(n) :
                if grid[i][j] == 1 :
                    first_x, first_y = i,j
                    break
        
        # recursively go from this point, find all cells of island A , add them to bfs_queue, mark them with 2
        def dfs(x,y) :
            grid[x][y] = 2 
            bfs_queue.append((x,y))
            for curr_x, curr_y in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)] :
                if 0 <= curr_x < n and 0 <= curr_y < n and grid[curr_x][curr_y] == 1 :
                    dfs(curr_x,curr_y)

        # add all land cells of island A to bfs_queue
        bfs_queue = []
        dfs(first_x,first_y)

        # set distance
        distance = 0

        # bfs to find the shorted distance
        while bfs_queue :
            new_bfs = []
            for x, y in bfs_queue :
                for curr_x, curr_y in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)] :
                    if 0 <= curr_x < n and 0 <= curr_y < n :    
                        if grid[curr_x][curr_y] == 1 :
                            return distance 
                        elif grid[curr_x][curr_y] == 0 :
                            new_bfs.append((curr_x,curr_y))
                            grid[curr_x][curr_y] = -1 # make that bridge cell as visited

            # finishing the bfs, one round increment distance and reset the bfs_queue to the new set 
            bfs_queue = new_bfs
            distance += 1
