class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n=len(triangle)
        dp=[row[:] for row in triangle]
        for i in range(1,n):
            for j in range(i+1):
                if j==0:
                    dp[i][j]+=dp[i-1][j]
                elif j==i:
                    dp[i][j]+=dp[i-1][j-1]
                else:
                    dp[i][j]+=min(dp[i-1][j],dp[i-1][j-1])
        return min(dp[n-1])

        