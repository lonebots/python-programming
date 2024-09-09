'''
You are given two integers m and n, which represent the dimensions of a matrix.

You are also given the head of a linked list of integers.

Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise), starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.

Return the generated matrix.

 

Example 1:

Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
Explanation: The diagram above shows how the values are printed in the matrix.
Note that the remaining spaces in the matrix are filled with -1.

Example 2:

Input: m = 1, n = 4, head = [0,1,2]
Output: [[0,1,2,-1]]
Explanation: The diagram above shows how the values are printed from left to right in the matrix.
The last space in the matrix is set to -1.

 

Constraints:

    1 <= m, n <= 105
    1 <= m * n <= 105
    The number of nodes in the list is in the range [1, m * n].
    0 <= Node.val <= 1000

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        result =  [[-1 for _ in range(n)] for _ in range(m)]
        index_x = index_y = 0 
        movement = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        current_direction = 0

        while head is not None:
            result[index_x][index_y] = head.val
            new_index_x = index_x + movement[current_direction][0]
            new_index_y = index_y + movement[current_direction][1]
  
            # check for out of bound condtion then change direction
            if( min(new_index_x, new_index_y) < 0 or new_index_x >= m or new_index_y >= n or result[new_index_x][new_index_y] != -1):
                current_direction = (current_direction + 1) % 4
            
            index_x += movement[current_direction][0]
            index_y += movement[current_direction][1]

            head = head.next
    
        return result