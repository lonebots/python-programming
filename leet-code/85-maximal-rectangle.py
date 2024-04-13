'''
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

Example 1:

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.

Example 2:

Input: matrix = [["0"]]
Output: 0

Example 3:

Input: matrix = [["1"]]
Output: 1

 

Constraints:

    rows == matrix.length
    cols == matrix[i].length
    1 <= row, cols <= 200
    matrix[i][j] is '0' or '1'.
'''

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        r, c=len(matrix), len(matrix[0])
        if r==1 and c==1:
            if matrix[0][0]=='1': return 1
            else: return 0
        h=[0]*(c+1)
        maxArea=0

        for i, row  in enumerate(matrix):
            st=[-1] 
            row.append('0')
            for j, x in enumerate(row):
                # build h
                if x=='1': h[j]+=1
                else: h[j]=0
                # mononotonic stack has at leat element -1
                while len(st)>1 and (j==c or h[j]<h[st[-1]]):
                    m=st[-1]
                    st.pop()
                    w=j-st[-1]-1
                    area=h[m]*w
                    maxArea=max(maxArea, area)
                st.append(j)
        return maxArea

        