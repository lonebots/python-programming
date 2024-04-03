'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

 

Constraints:

    m == board.length
    n = board[i].length
    1 <= m, n <= 6
    1 <= word.length <= 15
    board and word consists of only lowercase and uppercase English letters.

'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def dfs(r, c, curr) : 
            if curr == len(word) :
                return True
            
            if r < 0 or c < 0 or r >= rows or c >= cols or word[curr] != board[r][c] or (r,c) in visited:
                return False 
            
            visited.add((r,c))

            check = (dfs(r+1, c, curr+1)  or 
                    dfs(r-1, c, curr+1)  or
                    dfs(r, c+1, curr+1) or 
                    dfs(c, c-1, curr+1))

            visited.remove((r,c))

            return check 
        
        for row in range(rows) :
            for col in range(cols) :
                if dfs(row, col, 0) :
                    return True
        
        return False