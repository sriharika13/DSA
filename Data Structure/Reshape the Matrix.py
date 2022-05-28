# LeetCode: 566.Reshape the Matrix

'''In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.'''


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        import numpy as np
        x=len(mat)
        y=len(mat[0])
        if (x*y!=r*c):
            return mat
        res=[[0 for _ in range(c)] for _ in range(r)]   #list comorehensions very useful in this time
        # print(res)
        row=0
        col=0
        for i in range(x):
            for j in range(y):
                res[row][col]=mat[i][j]
                # print(res)
                col+=1
                if col==c:
                    row+=1
                    col=0
        return (res)
     #time : O(matrix dimension:x*y)
    #space: O(r*c)
        
