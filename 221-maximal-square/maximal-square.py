class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        maxedge=0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if col==0 or row==0:
                    maxedge=max(maxedge,int(matrix[row][col]))
                elif matrix[row][col]=='1':
                    matrix[row][col]=min(int(matrix[row][col-1]),
                    int(matrix[row-1][col]),
                    int(matrix[row-1][col-1]))+1
                    maxedge=max(maxedge,matrix[row][col])
                
        return maxedge**2
