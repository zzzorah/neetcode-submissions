class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def dp(n):
            if n == 1:
                return 1
            elif n == 2:
                return 2

            if n not in cache:
                cache[n] = dp(n - 2) + dp(n - 1)

            return cache[n]

            # return dp(n - 2) + dp(n - 1)

        return dp(n)