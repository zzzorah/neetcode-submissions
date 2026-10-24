class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(n):
            if n == 1:
                return 1
            elif n == 2:
                return 2

            return dp(n - 2) + dp(n - 1)

        return dp(n)