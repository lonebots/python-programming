'''
An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '. These characters divide the square into contiguous regions.

Given the grid grid represented as a string array, return the number of regions.

Note that backslash characters are escaped, so a '\' is represented as '\\'.

 

Example 1:

Input: grid = [" /","/ "]
Output: 2

Example 2:

Input: grid = [" /","  "]
Output: 1

Example 3:

Input: grid = ["/\\","\\/"]
Output: 5
Explanation: Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.

 

Constraints:

    n == grid.length == grid[i].length
    1 <= n <= 30
    grid[i][j] is either '/', '\', or ' '.
'''


class Solution:
    DIRECTION = [(1,0),(0,1),(-1,0),(0,-1)]
    def regionsBySlashes(self, grid: List[str]) -> int:
        grid_size = len(grid)
        # create new expanded_grid 
        expanded_grid_size = 3 * grid_size
        expanded_grid = [[0] * expanded_grid_size for _ in range(expanded_grid_size)]

        # fill the expanded grid
        for i in range(grid_size):
            for j in range(grid_size):
                base_row = 3 * i 
                base_col = 3 * j

                # handle different cases
                if grid[i][j] == "\\":
                    # mark diagonal for back slash
                    expanded_grid[base_row][base_col] = 1 
                    expanded_grid[base_row + 1][base_col + 1] = 1
                    expanded_grid[base_row + 2][base_col + 2] = 1
                elif grid[i][j] == "/":
                    # mark the diagonal for forward slash 
                    expanded_grid[base_row][base_col + 2] = 1 
                    expanded_grid[base_row + 1][base_col + 1] = 1
                    expanded_grid[base_row + 2][base_col] = 1
        
        # set the region count
        region_count = 0

        # activate the flood fill algorithm and start counting regions
        for row in range(expanded_grid_size):
            for col in range(expanded_grid_size):
                if expanded_grid[row][col] == 0:
                    self.flood_fill(expanded_grid, row, col)
                    # after filling the region; increment the region_count
                    region_count += 1 

        # finally return the number of regions
        return region_count


    def flood_fill(self, expanded_grid: List[List[int]], row: int,  col: int) -> None:
        queue = [(row, col)]

        #mark as visited
        expanded_grid[row][col] = 1 

        # bfs
        while queue : 
            current_cell = queue.pop(0)

            # get searching in all directions
            for direction in self.DIRECTION: 
                new_row = direction[0] + current_cell[0]
                new_col = direction[1] + current_cell[1]

                if(self.is_valid(expanded_grid, new_row, new_col)):
                    # mark as visited and add to queue for next set of search 
                    expanded_grid[new_row][new_col] = 1 
                    queue.append((new_row, new_col))
        

    def is_valid(self, expanded_grid: List[List[int]], row: int, col: int) -> bool:
        n = len(expanded_grid) 

        return ( 0 <= row < n and 0 <= col < n and expanded_grid[row][col] == 0)
        