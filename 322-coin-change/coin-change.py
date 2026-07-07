class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for remainder in range(1, amount + 1):
            for coin in coins:
                if remainder >= coin:
                    dp[remainder] = min(dp[remainder], 1 + dp[remainder - coin])
        return dp[amount] if dp[amount] != float('inf') else -1