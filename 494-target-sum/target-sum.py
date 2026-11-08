class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        total = sum(nums)   #backtracking is better
        if abs(target) > total:
            return 0
        if (total + target) % 2 != 0:
            return 0
        P = (total + target) // 2
        n = len(nums)
        dp = [[0] * (P + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(P + 1):
                # Don't include current element
                dp[i][j] = dp[i-1][j]
                # Include current element
                if j >= nums[i-1]:
                    dp[i][j] += dp[i-1][j-nums[i-1]]
        return dp[n][P]        