class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        dp=[row[:]for row in matrix]
        for i in range(1,m):
            for j in range(n):
                up=dp[i-1][j]
                left=float('inf')
                right=float('inf')
                if j>0:
                    left=dp[i-1][j-1]
                if j<n-1:
                    right=dp[i-1][j+1]
                dp[i][j]+=min(up,left,right)

        return min(dp[m-1])
        