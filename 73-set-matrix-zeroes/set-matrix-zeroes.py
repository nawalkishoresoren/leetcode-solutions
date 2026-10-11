class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = [0] * len(matrix)
        cols = [0] * len(matrix[0])

        for row in range(len(rows)):
            for col in range(len(cols)):
                if matrix[row][col] == 0:
                    rows[row] = 1
                    cols[col] = 1
        
        for row in range(len(rows)):
            for col in range(len(cols)):
                if rows[row] == 1 or cols[col] == 1:
                    matrix[row][col] = 0
        
        